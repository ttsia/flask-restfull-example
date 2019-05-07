# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: auth
# Created: 2019-05-07
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from flask import jsonify, g

from flask_httpauth import HTTPTokenAuth
from flask_bcrypt import Bcrypt
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

auth = HTTPTokenAuth("Flask-Auth")
bcrypt = Bcrypt()

token_serializer = Serializer("qwertyuiop", expires_in=3600)


@auth.error_handler
def default_auth_error():
    return jsonify({'message': "Unauthorized Access"})


@auth.verify_token
def verify_token(token):
    g.user = None
    print("token ", token)

    try:
        data = token_serializer.loads(token)
        print("data ", data)
    except:
        return False
    if 'username' in data:
        g.user = data['username']
        return True
    return False