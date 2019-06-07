from flask import current_app as app
from app.actions import Actions


class RunCommand:

    def run(self, request):
        command_text = request.form.get('text')
        command_text = command_text.split(' ')
        execute = self.execute_command(command_text, request)
        return execute

    def execute_command(self, command_text, request):
        get_allowed_commands = app.config['ALLOWED_COMMANDS']

        if command_text[0] not in get_allowed_commands:
            return app.config['INVALID_COMMAND_MESSAGE']

        if command_text[0] == 'help':
            return Actions.help()

        if command_text[0] == 'missing-profile-name':
            action = Actions()

            return action.users_without_profile_name(request)

        if command_text[0] == 'pr-report':
            action = Actions()

            return action.pull_request_report(request)

        if command_text[0] == 'issues-report':
            action = Actions()

            return action.issue_report(request)

        if command_text[0] == 'pr':
            action = Actions()
            length = len(command_text)

            if length == 2:
                return action.get_pull_request_for_repo(
                    command_text[1],
                    request
                )
            else:
                return {
                    "response_type": "in_channel",
                    'text': app.config['INVALID_COMMAND_MESSAGE']
                }
