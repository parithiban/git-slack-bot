import github
from collections import OrderedDict
from config import get_env
from flask import current_app as app
from operator import itemgetter
import datetime
import csv
import os


class GitApi(object):
    """Github Api to communicate with the git repo"""

    def __init__(self):
        self.git_token = get_env('GIT_TOKEN')
        self.git_instance = github.Github(self.git_token)

    def get_required_pull_request_reviews_count(self, repo, branch):
        try:
            total_review_count = (self.git_instance
                                  .get_repo(repo)
                                  .get_branch(branch)
                                  .get_required_pull_request_reviews()
                                  )
            return total_review_count.required_approving_review_count

        except Exception:
            return 0

    def get_pull_request(self, repo):
        org = get_env('ORGANISATION')
        repo_name = org + "/" + repo
        pull_requests = (self.git_instance
                         .get_repo(repo_name)
                         .get_pulls()
                         )

        if pull_requests.totalCount == 0:
            return False

        data = []
        for pr in pull_requests:
            reviews = pr.get_reviews()
            filtered = list(filter
                            (lambda x:
                             x.state == "APPROVED",
                             reviews
                             )
                            )

            required_review_count = (
                self.get_required_pull_request_reviews_count(
                    repo_name,
                    pr.base.ref
                )
            )

            data.append(OrderedDict([
                ("branch_name", pr.html_url),
                ("created_by", pr.user.name),
                ("required_reviews", required_review_count),
                ("approved_reviews", len(filtered))
            ]))

        return data

    def get_pull_request_count(self, repo_name):
        pull_requests = (self.git_instance
                         .get_repo(repo_name)
                         .get_pulls()
                         )
        return pull_requests.totalCount

    def get_issue_count(self, repo_name):
        issues = (self.git_instance
                  .get_repo(repo_name)
                  .get_issues()
                  )
        return issues.totalCount

    def get_issue_request_report_of_org(self):
        organisation = get_env('ORGANISATION')
        repos = self.git_instance.get_organization(organisation).get_repos()
        data = []

        for repo in repos:
            pull_request_count = self.get_pull_request_count(repo.full_name)
            issue_count = self.get_issue_count(repo.full_name)

            data.append(OrderedDict([
                ("name", repo.name),
                ("issues_count", issue_count - pull_request_count)
            ]))

        return sorted(data, key=itemgetter('name'))

    def get_pull_request_report_of_org(self):
        organisation = get_env('ORGANISATION')
        repos = self.git_instance.get_organization(organisation).get_repos()
        data = []

        for repo in repos:
            pull_request_count = self.get_pull_request_count(repo.full_name)
            data.append(OrderedDict([
                ("name", repo.name),
                ("pending_pull_request", pull_request_count)
            ]))

        return sorted(data, key=itemgetter('name'))

    def get_users_without_profile_name(self):
        organisation = get_env('ORGANISATION')
        members = self.git_instance.get_organization(organisation).get_members()
        i = 1
        users = []
        for member in members:
            if not member.name:
                users.append(OrderedDict([
                    ("No", i),
                    ("Login User", member.login),
                    ("Profile Link", member.html_url)
                ]))
                i = i + 1
        if len(users) == 0:
            return False
        return users

    def get_users_in_organisation(self):
        organisation = get_env('ORGANISATION')
        members = self.git_instance.get_organization(organisation).get_members()
        dir_path = os.path.dirname(os.path.realpath(__file__)) + "/../storage"
        users = []
        none = []
        for member in members:
            print(member.name)
            if member.name is not None:
                users.append([member.name, member.login, member.html_url])
            else:
                none.append([member.name, member.login, member.html_url])

        sorted = users.sort(key=lambda x: x[0])
        users.insert(0, ["User Name", "Login User", "Profile Link"])
        file_name = dir_path + "/git_users_" + \
            str(datetime.datetime.now()) + ".csv"
        result = users + none
        self.write_data_to_file(file_name, result)
        if len(users) == 0:
            return False
        return file_name

    def write_data_to_file(self, filename, csvData):
        with open(filename, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)

            csvFile.close()
