from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager

app = Flask('calculator_cash')
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def homepage():
    return "Hello world!"


if __name__ == '__main__':
    manager.run()
