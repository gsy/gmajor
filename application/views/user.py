# -*- coding: utf-8 -*-

from flask_login import (login_user, login_required, logout_user)
from flask import Blueprint, jsonify, request

from application.dao import user as user_dao
from application.views.schema import ApiResult

user_bp = Blueprint('user', __name__, url_prefix='/users')


@user_bp.route("/signup", method=["POST"])
def signup():
    data = request.json()
    email = data['email']
    username = data['username']
    password = data['password']

    user = user_dao.query_user(username=username)
    if user is not None:
        return jsonify(ApiResult(code=400, msg='username is duplicated'))

    user_dao.create_user(username=username, email=email, password=password)
    return jsonify(ApiResult())


@user_bp.route("/login", method=["POST"])
def login():
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


@user_bp.route("/oauth/wechat/login", method=["POST"])
def wx_login():
    '''申请微信权限中
    '''
    pass
