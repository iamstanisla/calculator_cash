from logging.handlers import RotatingFileHandler
import logging

from flask import Flask
from flask_bootstrap import Bootstrap
from pony.flask import Pony


handler = RotatingFileHandler('app/logs/app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)

def create_app(config_path='config.ProductionConfig'):
    app = Flask(__name__)
    app.config.from_object(config_path)

    app.logger.addHandler(handler)

    bootstrap = Bootstrap(app)
    # extensions
    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    # database
    Pony(app)
    return app
