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
            return jsonify({'error': 'Token is missing in the request, please try again.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token, please login again.'}), 403

        data = json.loads(request.data)

        if 'description' not in data:
            return jsonify({'error': 'Description is needed in the request.'}), 400
        if 'assignedToUid' not in data:
            return jsonify({'error': 'Assigned user is needed in the request.'}), 400

        if is_valid(data['assignedToUid']) is False:
            return jsonify({'error': 'Task assigned to an invalid user, please try again.'}), 400

        created_task = create_task(token, data)
        return jsonify({'uid': str(created_task.inserted_id)})

    except ValueError:
        return jsonify({'error': 'Error upon creating the task!'})


@task.route("/v0/tasks/createdby/", methods=["GET"])
def created_by():
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request, please try again.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token, please login again.'}), 403

        return fetch_created_task(token['id'])

    except ValueError:
        return jsonify({'error': 'Error upon fetching the tasks!'})


@task.route("/v0/tasks/assignedto/", methods=["GET"])
def assigned_to():
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request, please try again.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token, please login again.'}), 403

        return fetch_assigned_task(token['id'])
    except ValueError:
        return jsonify({'error': 'Error upon fetching the tasks!'})


@task.route("/v0/tasks/<taskUid>", methods=["PATCH"])
def update(taskUid):
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request, please try again.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token, please login again.'}), 403

        data = json.loads(request.data)
        if 'done' not in data:
            return jsonify({'error': '"Done" status not found in the request.'}), 400
        if is_valid(taskUid) is False:
            return jsonify({'error': 'Task not found.'}), 400

        list_task = fetch_assigned_task(token['id'])
        task_check = checking_task_in_list(list_task, taskUid)
        if task_check == 0:
            return jsonify({'error': 'The task status can only be changed by the user to who the task is assigned to.'}), 401

        return update_task(data, taskUid)
    except ValueError:
        return jsonify({'error': 'Error upon updating task!'})


@task.route("/v0/tasks/<taskUid>", methods=["DELETE"])
def delete_task(taskUid):
    try:
        token = validateJWT()
        if token == 400:
            return jsonify({'error': 'Token is missing in the request, please try again.'}), 401
        if token == 401:
            return jsonify({'error': 'Invalid authentication token, please login again.'}), 403
        if is_valid(taskUid) is False:
            return jsonify({'error': 'Task not found.'}), 400

        list_task = fetch_created_task(token['id'])
        task_check = checking_task_in_list(list_task, taskUid)
        if task_check == 0:
            return jsonify({'error': 'The task can only be deleted by its creator.'}), 401

        return delete(taskUid)
    except ValueError:
        return jsonify({'error': 'Error upon updating task!'})
