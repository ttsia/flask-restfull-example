# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: views
# Created: 2019-05-06
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
from bson.json_util import dumps
from database import users as users_db

from flask import Response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class UsersView(Resource):

    @jwt_required
    def get(self):
        response = users_db.get_all_users()
        return Response(dumps(response), mimetype='application/json')


class UsersLoginView(Resource):

    @jwt_required
    def get(self):
        response = users_db.get_user_by_id(get_jwt_identity())
        return Response(dumps(response), mimetype='application/json')

    def post(self):
        # TODO move parser to other file
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='Required field', required=True)
        parser.add_argument('password', help='Required field', required=True)
        args = parser.parse_args()

        existing_user = users_db.get_user_by_username(args['username'])
        if not existing_user:
            # Create new user
            hashed_password = bcrypt.generate_password_hash(args['password']).decode('utf-8')
            user_id = users_db.create_user({'username': args['username'], 'password': hashed_password})
            jwt = create_access_token(str(user_id))
            return {
                    'message': 'User <{0}> was successfully created: id={1}'.format(args['username'], user_id),
                    'jwt': jwt
                }
        else:
            # check password of existing user and create new jwt token
            if bcrypt.check_password_hash(existing_user[0]['password'], args['password']):
                jwt = create_access_token(str(existing_user[0]['_id']))
                return {
                    'message': 'User was successfully logged in',
                    'jwt': jwt
                }
            else:
                return {
                    'message': 'Invalid user password'
                }