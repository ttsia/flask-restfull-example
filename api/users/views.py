# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: views
# Created: 2019-05-06
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from api.db import get_client
from api.users.models import User

from flask import request, g
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from api.auth import auth, bcrypt


class UsersView(Resource):

    # @auth.login_required
    @jwt_required
    def get(self):
        client = get_client()
        UserDB = client.users
        response = UserDB.users.find()
        print(list(response))
        data = {
            'method': request.method,
            'username': auth.username(),
            # 'g': g.current_user,
            'get_auth': auth.get_auth()
        }

        return data

    @auth.login_required
    def post(self):
        data = {
            'method': request.method
        }
        return data


class UsersLoginView(Resource):

    @jwt_required
    def get(self):
        a = get_jwt_identity()
        print("a ", a)
        return {}

    def post(self):
        # TODO move parser to other file
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='Required field', required=True)
        parser.add_argument('password', help='Required field', required=True)
        args = parser.parse_args()
        print("parser ", args)
        # TODO database handling
        data = {
            'method': request.method,
            'username': auth.username()
        }

        hashed_password = bcrypt.generate_password_hash(args['password']).decode('utf-8')




        # client = get_client()
        # UserDB = client.users
        # response = UserDB.users.insert_one({'username': args['username'], 'password': hashed_password})
        # print("response ", response.inserted_id)
        #
        # create_access_token()
        jwt = create_access_token("qwerty")
        print("jwt ", jwt)
        return {
            'jwt': jwt
        }