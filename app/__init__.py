from flask import Flask


def create_app(config_path='config.ProductionConfig'):
    app = Flask(__name__)
    app.config.from_object(config_path)

    # extensions
    if app.debug:
        from flask_debugtoolbar import DebugToolbarExtension
        toolbar = DebugToolbarExtension()
        toolbar.init_app(app)

    return app
