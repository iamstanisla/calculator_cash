

class Config(object):
    # Определяет, включен ли режим отладки
    # В случае если включен, flask будет показывать
    # подробную отладочную информацию. Если выключен -
    # - 500 ошибку без какой либо дополнительной информации.
    DEBUG = False
    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = False
    # Случайный ключ, которые будет исползоваться для подписи
    # данных, например cookies.
    SECRET_KEY = 'ASDLFASHDFAHSDFJKLJL'
    # URI используемая для подключения к базе данных
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'darkly'
    UPLOAD_FOLDER = 'app/static/user_images'

class ProductionConfig(Config):
    PONY = {
    'provider': 'postgres',
    'user': 'test_countcash',
    'password': 'test1',
    'host': '127.0.0.1',
    'database': 'test_db',
    'create_db': True
}


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PONY = {
    'provider': 'sqlite',
    'filename': 'dev_db.sqlite3',
    'create_db': True
}
