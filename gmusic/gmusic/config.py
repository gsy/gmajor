# -*- coding: utf-8 -*-


class Config(object):
    SECRET_KEY = '!very_secret!'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_POOL_RECYCLE = 3600
    ORDER_TIMEOUT_SECONDS = 30
    ALLOWED_EXTENSIONS = set(['json'])
    ENABLE_ERP_AUTH = True

    # SENTRY_DSN = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://gmusic:gmusic@127.0.0.1:3306/gmusic?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = Config()
