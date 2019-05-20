# -*- coding: utf-8 -*-

from flask_login import (login_user, login_required, logout_user)
from flask import Blueprint, jsonify, request

from gmusic.dao import user as user_dao
from gmusic.view.schema import ApiResult

user_bp = Blueprint('user', __name__, url_prefix='/users')


@user_bp.route("/login", method=["POST"])
def login(username, password):
    data = request.json()
    username = data['username']
    password = data['password']

    user = user_dao.query_user(username=username)
    if user is None or not user_dao.check_password(username, password):
        return jsonify(ApiResult(code=401, msg='user not found or password error'))

    login_user(username, password)
    return jsonify(ApiResult())


@user_bp.route("/logout", method=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify(ApiResult())
