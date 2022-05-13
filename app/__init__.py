from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
  app = Flask(__name__)

  # Creating the app configurations
  app.config.from_object(config_options[config_name])

  # initializing flask extenstions
  bootstrap.init_app(app)

  # registering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  # setting config

  return app