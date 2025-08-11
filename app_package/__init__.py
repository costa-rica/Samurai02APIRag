from flask import Flask
# from app_package.config import config
from ._common.config import config
from ._common.utilities import custom_logger_init
import os
import logging
from logging.handlers import RotatingFileHandler
from pytz import timezone
from datetime import datetime


if not os.path.exists(os.path.join(os.environ.get('WEB_ROOT'),'logs')):
    os.makedirs(os.path.join(os.environ.get('WEB_ROOT'), 'logs'))

if not os.path.exists(os.path.join(os.environ.get('WEB_ROOT'),'logs')):
    os.makedirs(os.path.join(os.environ.get('WEB_ROOT'), 'logs'))

logger_init = custom_logger_init()

logger_init.info(f'--- Samurai 02 API RAG ---')


def create_app(config_for_flask = config):
    app = Flask(__name__)   
    app.config.from_object(config_for_flask)
    ############################################################################
    # create folders for PROJECT_RESOURCES
    create_folder(config_for_flask.PROJECT_RESOURCES_ROOT)
    ## website folders
    create_folder(config_for_flask.DIR_ASSETS)
    create_folder(config_for_flask.DIR_ASSETS_IMAGES)
    create_folder(config_for_flask.DIR_ASSETS_FAVICONS)

    ## RAG stuff
    create_folder(config_for_flask.PATH_TO_RAG_CONTEXT_DATA)
    create_folder(config_for_flask.PATH_TO_RAG_INDEX)

    ############################################################################

    from app_package.bp_main.routes import bp_main
    from app_package.bp_rag.routes import bp_rag

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_rag)

    return app


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger_init.info(f"created: {folder_path}")