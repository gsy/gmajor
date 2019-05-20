# -*- coding: utf-8 -*-

import click
import logging
import logging.config

from flask import Flask, cli

from application.model import db
from application.model import migrate


@click.command()
@cli.with_appcontext
def build_tables():
    db.create_all()


def create_app(config):
    app = Flask(__name__)
    configure_app(app, config)
    configure_blueprints(app)
    configure_logging(app, config)
    configure_error_handlers(app)
    return app


def configure_app(app, config):
    app.config.from_object(config)
    migrate.init_app(app, db)
    db.init_app(app)
    app.cli.add_command(build_tables)


def configure_blueprints(app):
    from application.views import blueprints

    for bp in blueprints:
        app.register_blueprint(bp)


def configure_logging(app, conf):
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': True,

        'formatters': {
            'console': {
                'format': '[%(asctime)-6s %(module)s.%(funcName)s.%(lineno)s] %(levelname)s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },

        'handlers': {
            'console': {
                'level': logging.INFO,
                'formatter': 'console',
                'class': 'logging.StreamHandler',
            },
            # 'sentry': {
            #     'level': 'ERROR',
            #     'class': 'raven.handlers.logging.SentryHandler',
            #     'dsn': conf.SENTRY_DSN,
            # },
        },


        'loggers': {
            '': {
                # 'handlers': ['console', 'sentry'],
                'handlers': ['console'],
                'propagate': False,
            },
        },
    })


def configure_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception(exception):
        print(exception)
