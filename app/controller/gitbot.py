from flask import Blueprint
from flask import jsonify, request
from app.utils.run_command import RunCommand


bot = Blueprint('bot', __name__)


@bot.route("/git", methods=["POST"])
def run():
    run_command = RunCommand()
    output = run_command.run(request)

    return jsonify(output), 200
