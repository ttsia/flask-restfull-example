# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: jwt_auth
# Created: 2019-05-10
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
JWT Auth SetUp
"""
from flask_jwt_extended import JWTManager

JWT = JWTManager()
BLACKLIST = set()


@JWT.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """
    :param decrypted_token:
    :return:
    """
    jti = decrypted_token['jti']
    return jti in BLACKLIST
