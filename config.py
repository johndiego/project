import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APPLICATION_ROOT = "/api"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Password@1@db/app"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Password@1@db/app"

class DevelopmentConfig(Config):
    DEBUG = True
    #'sqlite:///db.sqlite'

    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Password@1@db/app"
    SQLALCHEMY_ECHO = False
    #SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False