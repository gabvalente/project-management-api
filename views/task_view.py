from flask import Blueprint, request, jsonify
from controllers.task_controller import createTask, getUserNameByUId, fetchCreatedTask, fetchAssignedToTask
from database.__init__ import database
from models.user_model import User
import json
from controllers.user_controller import createUser, loginUser, fetchUsers
from helpers.token_validation import validateJWT

task = Blueprint("task", __name__)


@task.route("/v0/tasks/createTask", methods=["POST"])
def create():
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 400
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 401

        data = json.loads(request.data)

        if 'description' not in data:
            return jsonify({'error': 'Description is needed in the request.'}), 400
        if 'assignedToUid' not in data:
            return jsonify({'error': 'Assigned user is needed in the request.'}), 400
        # if not getUserNameByUId(data['assignedToUid']):
        #     return jsonify({'error': 'Assigned Uid is not valid.'}), 400

        createdTask = createTask(token, data)
        return jsonify({'uid': str(createdTask.inserted_id)})
    
    except ValueError:
        return jsonify({'error': 'Error creating task.'})


@task.route("/v0/tasks/createdby/", methods=["GET"])
def createdBy():
    token = validateJWT()
    if token == 400:
        return jsonify({'error': 'Token is missing in the request.'}), 400
    if token == 401:
        return jsonify({'error': 'Invalid authentication token.'}), 401

    return fetchCreatedTask(token['id'])


@task.route("/v0/tasks/assignedto/", methods=["GET"])
def assignedTo():
    token = validateJWT()
    if token == 400:
        return jsonify({'error': 'Token is missing in the request.'}), 400
    if token == 401:
        return jsonify({'error': 'Invalid authentication token.'}), 401

    return fetchAssignedToTask(token['id'])


@task.route("/v0/tasks/<taskUid>", methods=["PATCH"])
def updatetask(taskUid):
    return "fetch task linnk"


@task.route("/v0/tasks/<taskUid>", methods=["DELETE"])
def deleteTask(taskUid):
    return "delete link"
