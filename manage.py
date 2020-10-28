from app import create_app
from flask_script import Manager


app = create_app('config.DevelopmentConfig')


@app.route('/')
def test():
    return 'Hello World'


manager = Manager(app)


if __name__ == '__main__':
    manager.run()
