from flask import Blueprint
from flask import render_template, current_app, send_from_directory
import os
from app_package._common.utilities import custom_logger


logger_bp_main = custom_logger('bp_main.log')
bp_main = Blueprint('bp_main', __name__)


@bp_main.get("/ping")
def ping():
    logger_bp_main.info("-- in ping route --")
    return {"ok": True}

@bp_main.get("/echo")
def echo():
    logger_bp_main.info("-- in echo route --")
    return jsonify({
        "method": request.method,
        "headers": {k: v for k, v in request.headers.items()},
        "args": request.args.to_dict()
    })

@bp_main.route("/", methods=["GET","POST"])
def home():
    logger_bp_main.info(f"-- in home page route --")

    return render_template('main/home.html')

# Website Assets static data
@bp_main.route('/website_assets_favicon/<filename>')
def website_assets_favicon(filename):
    logger_bp_main.info("-- in website_assets_favicon -")
    file_to_server = os.path.join(current_app.config.get('DIR_ASSETS_FAVICONS'), filename)
    logger_bp_main.info(f"file_to_server: {file_to_server}")
    return send_from_directory(current_app.config.get('DIR_ASSETS_FAVICONS'), filename)


