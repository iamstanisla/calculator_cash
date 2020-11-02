from flask import Flask
from flask_bootstrap import Bootstrap


def create_app(config_path='config.ProductionConfig'):
    app = Flask(__name__)
    app.config.from_object(config_path)

    bootstrap = Bootstrap(app)
    # extensions
    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    return app
