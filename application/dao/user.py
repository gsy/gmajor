# -*- coding: utf-8 -*-

from application.model import db
from application.model.user import User


def create_user(username, email, password):
    new_user = User(
        username=username,
        email=email,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user


def query_user(username):
    return User.query.filter_by(username=username).first()


def check_password(username, password):
    user = query_user(username)
    if user:
        return user.password == password

    return False
