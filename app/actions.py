from app.utils.slackhelper import SlackHelper
from flask import current_app as app
from app.utils.githelper import GitApi
from app.worker import (
    pull_request_of_given_repo,
    github_users_without_profile_name,
    github_pull_request_report,
    get_users_in_organisation,
    github_issue_report
)


class Actions:
    def __init__(self):
        self.slack_helper = SlackHelper()
        self.git_helper = GitApi()

    @staticmethod
    def help():
        """
        Return the Available commands in the system and their usage format
        """
        return {
            "response_type": "in_channel",
            'text': app.config['HELP_MESSAGE']
        }

    def users_without_profile_name(self, request):
        data = {
            'channel_id': request.form.get('channel_id'),
            'user_id': request.form.get('user_id'),
            'response_url': request.form.get('response_url')
        }

        github_users_without_profile_name.queue(data, timeout=60 * 7)

        return {
            "response_type": "in_channel",
            'text': app.config['IMMEDIATE_RESPONSE']
        }

    def get_pull_request_for_repo(self, repo_name, request):
        data = {
            'channel_id': request.form.get('channel_id'),
            'user_id': request.form.get('user_id'),
            'repo': repo_name,
            'response_url': request.form.get('response_url')
        }
        pull_request_of_given_repo.queue(data)

        return {
            "response_type": "in_channel",
            'text': app.config['IMMEDIATE_RESPONSE']
        }

    def pull_request_report(self, request):
        data = {
            'channel_id': request.form.get('channel_id'),
            'user_id': request.form.get('user_id'),
            'response_url': request.form.get('response_url'),
        }

        github_pull_request_report.queue(data)

        return {
            "response_type": "in_channel",
            'text': app.config['IMMEDIATE_RESPONSE']
        }

    def issue_report(self, request):
        data = {
            'channel_id': request.form.get('channel_id'),
            'user_id': request.form.get('user_id'),
            'response_url': request.form.get('response_url'),
        }

        github_issue_report.queue(data)

        return {
            "response_type": "in_channel",
            'text': app.config['IMMEDIATE_RESPONSE']
        }

    def get_users_in_organisation(self, request):
        data = {
            'channel_id': request.form.get('channel_id'),
            'user_id': request.form.get('user_id'),
            'response_url': request.form.get('response_url')
        }

        get_users_in_organisation.queue(data, timeout=60 * 7)

        return {
            "response_type": "in_channel",
            'text': app.config['IMMEDIATE_RESPONSE']
        }
