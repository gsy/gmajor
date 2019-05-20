# -*- coding: utf-8 -*-

from application.model.user import User


def query_user(username):
    return User.query.filter_by(username=username).first()


def check_password(username, password):
    user = query_user(username)
    if user:
        return user.password == password

    return False
