from flask import Blueprint, request, jsonify
from controllers.task_controller import create_task, fetch_created_task, fetch_assigned_task, update_task, delete, \
 checking_task_in_list
import json
from helpers.token_validation import validateJWT
from helpers.is_valid_oi import is_valid

task = Blueprint("task", __name__)


@task.route("/v0/tasks/createTask", methods=["POST"])
def create():
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 403

        data = json.loads(request.data)

        if 'description' not in data:
            return jsonify({'error': 'Description is needed in the request.'}), 400
        if 'assignedToUid' not in data:
            return jsonify({'error': 'Assigned user is needed in the request.'}), 400

        if is_valid(data['assignedToUid']) is False:
            return jsonify({'error': 'The user who was assigned the task is invalid.'}), 400

        created_task = create_task(token, data)
        return jsonify({'uid': str(created_task.inserted_id)})

    except ValueError:
        return jsonify({'error': 'Error creating task.'})


@task.route("/v0/tasks/createdby/", methods=["GET"])
def created_by():
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 403

        return fetch_created_task(token['id'])

    except ValueError:
        return jsonify({'error': 'Error fetching task.'})


@task.route("/v0/tasks/assignedto/", methods=["GET"])
def assigned_to():
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 403

        return fetch_assigned_task(token['id'])
    except ValueError:
        return jsonify({'error': 'Error fetching task.'})


@task.route("/v0/tasks/<taskUid>", methods=["PATCH"])
def update(taskUid):
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 403

        data = json.loads(request.data)
        if 'done' not in data:
            return jsonify({'error': 'Done is needed in the request.'}), 400
        if is_valid(taskUid) is False:
            return jsonify({'error': 'The task does not exits.'}), 400

        list_task = fetch_assigned_task(token['id'])
        task_check = checking_task_in_list(list_task, taskUid)
        if task_check == 0:
            return jsonify({'error': 'This task is not assigned to you so you cannot update'}), 401

        return update_task(data, taskUid)
    except ValueError:
        return jsonify({'error': 'Error updating task.'})


@task.route("/v0/tasks/<taskUid>", methods=["DELETE"])
def delete_task(taskUid):
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 403
        if is_valid(taskUid) is False:
            return jsonify({'error': 'The task does not exits.'}), 400

        list_task = fetch_created_task(token['id'])
        task_check = checking_task_in_list(list_task, taskUid)
        if task_check == 0:
            return jsonify({'error': 'This task is not created by you so you cannot delete'}), 401

        return delete(taskUid)
    except ValueError:
        return jsonify({'error': 'Error deleting task.'})
