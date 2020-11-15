from logging.handlers import RotatingFileHandler
from logging import Formatter
import logging

from flask import Flask
from flask_bootstrap import Bootstrap
from pony.flask import Pony

log = logging.getLogger('werkzeug')

handler = RotatingFileHandler('app/logs/app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
fmt = '%(asctime)s %(name)s %(levelname)s %(message)s'
fmt_two = "[%(asctime)s] %(levelname)s in <%(name)s> |%(filename)s:%(lineno)d-%(funcName)s| -> \'%(message)s\' "
formatter = Formatter(fmt=fmt_two)
handler.setFormatter(formatter)

def create_app(config_path='config.ProductionConfig'):
    app = Flask(__name__)
    app.config.from_object(config_path)

    log.addHandler(handler)

    bootstrap = Bootstrap(app)
    # extensions
    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    # database
    Pony(app)
    return app
