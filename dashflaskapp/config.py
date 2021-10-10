class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '4f2f005ca672378f8684b8daa10be810'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    CORS_HEADERS = 'Content-Type'

class DevelopmentConfig(Config):
    DEBUG = True

class StagingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
