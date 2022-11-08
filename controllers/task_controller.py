from flask import jsonify
from models.user_model import User
from models.task_model import Task
import bcrypt
from database.__init__ import database
import app_config as config
from datetime import datetime, timedelta
import jwt
from controllers.user_controller import createUser, loginUser, fetchUsers
from bson.objectid import ObjectId


def getUserNameByUId(Uid):
    collection = database.dataBase[config.CONST_USER_COLLECTION]
    userInfo = collection.find_one({"_id": ObjectId(Uid)})
    return userInfo['name']


def createTask(userInformation, taskInformation):
    newTask = None
    try:
        newTask = Task()
        newTask.description = taskInformation['description']
        newTask.createdByUid = userInformation['id']
        newTask.createdByName = getUserNameByUId(userInformation['id'])
        newTask.assignedToUid = taskInformation['assignedToUid']
        newTask.assignedToName = getUserNameByUId(taskInformation['assignedToUid'])

        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        createdTask = collection.insert_one(newTask.__dict__)
        return createdTask
    except Exception as err:
        raise ValueError('Error on creating task: ', err)


def fetchCreatedTask(Uid):
    try:
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        createdTasks = []

        for task in collection.find():
            if str(task['createdByUid']) == str(Uid):
                currentTask = {}
                currentTask.update({'uid': str(task['_id'])})
                currentTask.update({'description': task['description']})
                currentTask.update({'createdByUid': str(task['createdByUid'])})
                currentTask.update({'createdByName': task['createdByName']})
                currentTask.update({'assignedToUid': str(task['assignedToUid'])})
                currentTask.update({'assignedToName': task['assignedToName']})
                createdTasks.append(currentTask)

        return createdTasks

    except Exception as err:
        raise ValueError("Error when trying to fetch users: ", err)


def fetchAssignedToTask(Uid):
    try:
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        createdTasks = []

        for task in collection.find():
            if str(task['assignedToUid']) == str(Uid):
                currentTask = {}
                currentTask.update({'uid': str(task['_id'])})
                currentTask.update({'description': task['description']})
                currentTask.update({'createdByUid': task['createdByUid']})
                currentTask.update({'createdByName': task['createdByName']})
                currentTask.update({'assignedToUid': task['assignedToUid']})
                currentTask.update({'assignedToName': task['assignedToName']})
                createdTasks.append(currentTask)

        return createdTasks

    except Exception as err:
        raise ValueError("Error when trying to fetch users: ", err)
