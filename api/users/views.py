# -*- coding: utf-8 -*-
#
# Project name: flask-restfull-example
# File name: views
# Created: 2019-05-06
#
# Author: Liubov M. <liubov.mikhailova@gmail.com>
"""
Users endpoints handling
"""
from bson.json_util import dumps
from flask import Response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, \
    jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from flask_restful import Resource, reqparse

from database import users as users_db
from settings.jwt_auth import BLACKLIST

BCRYPT = Bcrypt()


class UsersView(Resource):
    """
    Users list
    """

    @jwt_required
    def get(self):
        """
        Getting all users
        """
        response = users_db.get_all_users()
        return Response(dumps(response), mimetype='application/json')


class UserView(Resource):
    """
    User info
    """

    @jwt_required
    def get(self):
        """
        Getting info about user from JWT
        """
        response = users_db.get_user_by_id(get_jwt_identity())
        return Response(dumps(response), mimetype='application/json')


class UserLogout(Resource):
    """
    User log out
    """

    @jwt_required
    def post(self):
        """
        User log out
        """
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        response = {
            'message': "Successfully logged out"
        }
        return Response(dumps(response), mimetype='application/json')


class UsersLoginView(Resource):
    """
    User registration and login
    """

    def post(self):
        """
        User registration and login
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='Required field', required=True)
        parser.add_argument('password', help='Required field', required=True)
        args = parser.parse_args()

        existing_user = users_db.get_user_by_username(args['username'])
        if not existing_user:
            # Create new user
            hashed_password = BCRYPT.generate_password_hash(args['password']).decode('utf-8')
            user_id = users_db.create_user(
                {
                    'username': args['username'],
                    'password': hashed_password
                }
            )

            # Use create_access_token() and create_refresh_token()
            # to create our access and refresh tokens
            response, status = {
                'message': 'User <{0}> was successfully created: id={1}'.format(
                    args['username'], user_id
                ),
                'access_token': create_access_token(identity=str(user_id)),
                'refresh_token': create_refresh_token(identity=str(user_id))
            }, 201
        else:
            # check password of existing user and create new jwt token
            if BCRYPT.check_password_hash(existing_user[0]['password'], args['password']):
                response, status = {
                    'message': 'User <{0}> was successfully logged in'.format(
                        existing_user[0]['username']
                    ),
                    'access_token': create_access_token(identity=str(existing_user[0]['_id'])),
                    'refresh_token': create_refresh_token(identity=str(existing_user[0]['_id']))
                }, 200
            else:
                response, status = {
                    'message': 'Invalid user password'
                }, 400

        return Response(dumps(response), status=status, mimetype='application/json')


class TokenRefresh(Resource):
    """
    Refresh token handler
    """

    @jwt_refresh_token_required
    def post(self):
        """
        The jwt_refresh_token_required decorator insures a valid refresh
        token is present in the request before calling this endpoint. We
        can use the get_jwt_identity() function to get the identity of
        the refresh token, and use the create_access_token() function again
        to make a new access token for this identity.
        """
        current_user_id = get_jwt_identity()
        new_token = create_access_token(identity=current_user_id)
        response, status = {
            'message': 'Access token was successfully refreshed',
            'access_token': new_token
        }, 200
        return Response(dumps(response), status=status, mimetype='application/json')
