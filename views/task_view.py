from flask import Blueprint, request, jsonify
from controllers.task_controller import getUserNameByUId
from database.__init__ import database
from models.task_model import Task
import json
from controllers.task_controller import createTask
from helpers.token_validation import validateJWT
from helpers.getToken import getToken
from bson.objectid import ObjectId
import app_config as config

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
        # collection = database.dataBase[config.CONST_USER_COLLECTION]
        # name = collection.find_one({"_id": ObjectId("data['assignedToUid']")})
        print(token['id'])
        # return name
        # token1 = getToken()
        # print(token)
        
        createdTask = createTask(data)
        
        # if not createdTask.inserted_id:
        #     return jsonify({'error': 'Something wrong happened when creating task.'}), 500

        return jsonify({'uid': str(createdTask.inserted_id)})
        
    except ValueError:
        return jsonify({'error': 'Error creating task.'})

# @task.route("/v0/tasks/updateTask", methods=["POST"])
# def updateTask(): 
#     try:
#         data = json.load(request.data)
#         if 'title' not in data: 
#             return jsonify({'error': 'Title is needed in the request.'}), 400
#         markingTask = markDone(data)
#         return jsonify({'message': 'the task is succesfully marked done'})
#     except ValueError: 
#         return jsonify({'error': 'Error while changing status of the task.'})
 
 
@task.route("/v0/tasks/createdBy", methods=["GET"])
def createdBy(): 
    return "created by link works"
 
 
@task.route("/v0/tasks/assignedTo", methods=["GET"])
def assignedTo(): 
    return "assigned to link works"



@task.route("/v0/tasks/<taskUid>", methods=["PATCH"])
def updatetask(taskUid): 
    return "update link works"



@task.route("/v0/tasks/<taskUid>", methods=["DELETE"])
def deleteTask(taskUid): 
    return "delete link works"


        
