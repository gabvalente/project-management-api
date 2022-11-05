from flask import jsonify
from models.user_model import User
from models.task_model import Task
import bcrypt
from database.__init__ import database
import app_config as config
from datetime import datetime, timedelta
import jwt


def createTask(taskInformation):
    newTask = None
    try:
        newTask = Task()
        newTask.title = taskInformation['name'].lower()
        newTask.description = taskInformation['description'].lower()
        newTask.deadline = taskInformation['deadline']
        newTask.assign = taskInformation['assign']
        newTask.message = taskInformation['message']

        collection = database.dataBase[config.CONST_TASK_COLLECTION]

        if collection.find_one({'name': newTask.name}):
            return "This name task is already used"

        createdTask = collection.insert_one(newTask.__dict__)

        return createdTask
    except Exception as err:
        raise ValueError('Error on creating task: ', err)

def fetchTask():
    try:
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        tasks = []

        for task in collection.find():
            currentTask = {}
            currentTask.update({'name': str(task['_id'])})
            currentTask.update({'description': str['email']})
            currentTask.update({'name': user['name']})
            users.append(currentUser)
        
        return users

    except Exception as err:
        raise ValueError("Error when trying to fetch users: ", err)