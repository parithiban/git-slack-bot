from flask import current_app as app
from tabulate import tabulate
from flask_rq2 import RQ
from config import get_env
from app.utils.githelper import GitApi
from app.utils.slackhelper import SlackHelper

rq = RQ()
__slack_helper = SlackHelper()
__git_helper = GitApi()


@rq.job
def pull_request_of_given_repo(args):
    try:
        result = __git_helper.get_pull_request(args['repo'])

        if not result:
            message = app.config['NO_PULL_REQUEST'] + ' for ' + args['repo']
            __slack_helper.send_message(message, args['response_url'])
        else:
            n = 25
            """Chunk the big list into group of 20 as it would be neater to send slack message """
            message = "Hello <@" + args['user_id'] + "> \n"
            message += " *Pending Pull request in " + args['repo'] + "*\n"
            chunk_lists = chunk_list_group(result, n)

            __slack_helper.send_message(message, args['response_url'])

            for chunk_list in chunk_lists:
                message = "```\n" + tabulate(
                    chunk_list,
                    headers="keys",
                    tablefmt="psql") + "\n```\n"
                __slack_helper.send_message(message, args['response_url'])
    except Exception:
        exception = "Hello <@" + args['user_id'] + \
            "> there is a problem  with your request. Please contact the administrator"
        __slack_helper.send_message(exception, args['response_url'])


@rq.job
def github_users_without_profile_name(args):
    try:
        result = __git_helper.get_users_without_profile_name()

        if not result:
            message = app.config['USERS_WITHOUT_PROFILE_NAME']
            __slack_helper.send_message(message, args['response_url'])
        else:
            n = 25
            """Chunk the big list into group of 20 as it would be neater to send slack message """
            message = "Hello <@" + args['user_id'] + "> \n"
            message += "*List of users whose profile name is not filled* \n"
            chunk_lists = chunk_list_group(result, n)

            __slack_helper.send_message(message, args['response_url'])

            for chunk_list in chunk_lists:
                message = "```\n" + tabulate(
                    chunk_list,
                    headers="keys",
                    tablefmt="psql") + "\n```\n"
                __slack_helper.send_message(message, args['response_url'])
    except Exception:
        exception = "Hello <@" + args['user_id'] + \
            "> there is a problem  with your request. Please contact the administrator"
        __slack_helper.send_message(exception, args['response_url'])


@rq.job
def github_pull_request_report(args):
    try:
        result = __git_helper.get_pull_request_report_of_org()
        n = 25
        """Chunk the big list into group of 20 as it would be neater to send slack message """
        message = "Hello <@" + args['user_id'] + "> \n"
        message += "*Pull request report for " + \
            get_env('ORGANISATION') + "* \n"
        chunk_lists = chunk_list_group(result, n)

        __slack_helper.send_message(message, args['response_url'])

        for chunk_list in chunk_lists:
            message = "```\n" + tabulate(
                chunk_list,
                headers="keys",
                tablefmt="psql") + "\n```\n"
            __slack_helper.send_message(message, args['response_url'])
    except Exception:
        exception = "Hello <@" + args['user_id'] + \
            "> there is a problem  with your request. Please contact the administrator"
        __slack_helper.send_message(exception, args['response_url'])


@rq.job
def github_issue_report(args):
    try:
        result = __git_helper.get_issue_request_report_of_org()
        n = 25
        """Chunk the big list into group of 20 as it would be neater to send slack message """
        message = "Hello <@" + args['user_id'] + "> \n"
        message += "*Issues report for " + get_env('ORGANISATION') + "* \n"
        chunk_lists = chunk_list_group(result, n)
        __slack_helper.send_message(message, args['response_url'])

        for chunk_list in chunk_lists:
            message = "```\n" + tabulate(
                chunk_list,
                headers="keys",
                tablefmt="psql") + "\n```\n"
            __slack_helper.send_message(message, args['response_url'])
    except Exception:
        exception = "Hello <@" + args['user_id'] + \
            "> there is a problem  with your request. Please contact the administrator"
        __slack_helper.send_message(exception, args['response_url'])


@rq.job
def get_users_in_organisation(args):
    try:
        result = __git_helper.get_users_in_organisation()

        if not result:
            message = app.config['NO_USERS_IN_ORGANISATION']
            __slack_helper.send_message(message, args['response_url'])
        else:
            n = 30
            message = "Hello <@" + args['user_id'] + "> \n"
            __slack_helper.send_as_attachment(
                result, args['channel_id'])
    except Exception as e:
        print("exception handling")
        print(e)
        exception = "Hello <@" + args['user_id'] + \
            "> there is a problem  with your request. Please contact the administrator"
        __slack_helper.send_message(exception, args['response_url'])


def chunk_list_group(input, n):
    return [input[i * n: (i + 1) * n]
            for i in range((len(input) + n - 1) // n)]
