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
        newTask.createdByUid: str = userInformation['id']
        newTask.createdByName: str = getUserNameByUId(userInformation['id'])
        newTask.assignedToUid: str = taskInformation['assignedToUid']
        newTask.assignedToName: str = getUserNameByUId(taskInformation['assignedToUid'])
                
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        createdTask = collection.insert_one(newTask.__dict__)
        return createdTask
    except Exception as err:
        raise ValueError('Error on creating task: ', err)
    
