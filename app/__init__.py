from flask import Flask
from config.env import app_env
from app.controller.gitbot import bot
import rq_dashboard


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')
    app.register_blueprint(bot, url_prefix='/')
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/queue")

    return app
