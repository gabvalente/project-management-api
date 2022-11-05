from flask import Blueprint, request, jsonify
from database.__init__ import database
from models.user_model import User
import json
from controllers.user_controller import createUser, loginUser, fetchUsers
from helpers.token_validation import validateJWT

user = Blueprint("user", __name__)

@user.route("/v0/users/signup", methods=["POST"])
def create():
    try:
        data = json.loads(request.data)

        if 'email' not in data:
            return jsonify({'error': 'Email is needed in the request.'}), 400
        if 'password' not in data:
            return jsonify({'error': 'Password is needed in the request.'}), 400
        if 'name' not in data:
            return jsonify({'error': 'Name is needed in the request.'}), 400

        createdUser = createUser(data)

        if createdUser == "Duplicated User":
            return jsonify({'error': 'There is already an user with this email.'}), 400
        
        if not createdUser.inserted_id:
            return jsonify({'error': 'Something wrong happened when creating user.'}), 500

        return jsonify({'uid': str(createdUser.inserted_id)})
    except ValueError:
        return jsonify({'error': 'Error creating user.'}), 400

@user.route("/v0/users/login", methods=["POST"])
def login():
    try:
        data = json.loads(request.data)

        if 'email' not in data:
            return jsonify({'error': 'Email is needed in the request.'}), 400
        if 'password' not in data:
            return jsonify({'error': 'Password is needed in the request.'}), 400

        loginAttempt = loginUser(data)

        if loginAttempt == "Invalid email":
            return jsonify({'error': 'Email not found.'}), 401

        if loginAttempt == "Invalid password":
            return jsonify({'error': 'Invalid Credentials'}), 401

        return jsonify({'token': loginAttempt.json['token'], 'expiration': loginAttempt.json['expiration'], 'loggedUser': loginAttempt.json['loggedUser']})


    except ValueError:
        return jsonify({'error': 'Error login user.'})

@user.route("/v0/users/all", methods=["GET"])
def fetch():
    try:
        token = validateJWT()

        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 400
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 401

        return fetchUsers()
    except ValueError:
        return jsonify({'error': 'Error on fetching users, try again.'})