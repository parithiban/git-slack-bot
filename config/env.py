from config import get_env


class EnvConfig(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    ALLOWED_COMMANDS = [
        'help',
        'pr-report',
        'issues-report',
        'missing-profile-name',
        'pr',
        'get-users-list'
    ]
    HELP_MESSAGE = "Available Commands: \n \
`/git pr git-slack-bot` to get the open pull request of the speific repo \n \
`/git pr-report` to get pull request report of the entire organisation \n \
`/git issues-report` to get issue report of the entire organisation \n \
`/git missing-profile-name` to get the list of users who have not filled in their profile name \n \
`/git get-users-list` to get the list of users in the organisation"


INVALID_COMMAND_MESSAGE = 'Invalid Command Sent - `/git help` for available commands'
NO_PULL_REQUEST = 'No pull request available'
IMMEDIATE_RESPONSE = "Your request is in progress. Please wait!!"
USERS_WITHOUT_PROFILE_NAME = "There is no user without the profile name"
NO_USERS_IN_ORGANISATION = "There is no user in the organisation"


class DevelopmentEnv(EnvConfig):
    """Configurations for Development."""
    DEBUG = True
    RQ_REDIS_URL = 'redis://127.0.0.1:6379'
    RQ_DASHBOARD_REDIS_URL = 'redis://127.0.0.1:6379'
    RQ_DASHBOARD_REDIS_HOST = '127.0.0.1'
    RQ_DASHBOARD_REDIS_PORT = '6379'
    RQ_DASHBOARD_REDIS_PASSWORD = 'redis'
    RQ_DASHBOARD_POLL_INTERVAL = '2500'
    RQ_QUEUES = ['default']


class StagingEnv(EnvConfig):
    """Configurations for Staging."""
    DEBUG = True


class ProductionEnv(EnvConfig):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_env = {
    'development': DevelopmentEnv,
    'staging': StagingEnv,
    'production': ProductionEnv,
}
