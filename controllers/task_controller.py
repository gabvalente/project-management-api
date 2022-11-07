from flask import jsonify
from models.user_model import User
import bcrypt
from database.__init__ import database
import app_config as config
from datetime import datetime, timedelta
import jwt

# def generateHashPassword(password):
#    salt = bcrypt.gensalt()
#    hashedPassword = bcrypt.hashpw(password.encode("utf-8"), salt)
#    return hashedPassword

def createTask(token, taskInformation):

    newTask = None

    try:

        newTask = Task()
        newTask.description = taskInformation['description'].lower()
        newTask.createdByUid: str = token['id']
       # newTask.createdByName: str = getUserNameByUId(newTask.createdByUid)
        newTask.assignedToUid: str = taskInformation['assignedToUid']
       # newTask.assignedToName: str = getUserNameByUId(newTask.assignedToUid)
             
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        createdTask = collection.insert_one(newTask.__dict__)
        return createdTask
    except Exception as err:
        raise ValueError('Error on creating task: ', err)
        
   

        

        
    

