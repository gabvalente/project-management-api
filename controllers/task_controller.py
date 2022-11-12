from flask import jsonify
from models.task_model import Task
from database.__init__ import database
import app_config as config
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
        raise ValueError("Error when trying to fetch tasks: ", err)


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
        raise ValueError("Error when trying to fetch tasks: ", err)

def checking_task_in_list(task_list, task_uid):
    count=0;
    for task in task_list: 
        if str(task['uid']) == str(task_uid):
            count =count+1
    if count==0:
        return 0

def updateTask(token, Uid):
    try: 
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        taskToUpdate = collection.find_one({"_id": ObjectId(Uid)})
        if str(taskToUpdate['assignedToUid'])!=str(token['id']):
            return jsonify({'error': "User can only change status when task is assigned to them."})
        collection.update_one({"_id":taskToUpdate["_id"]}, {"$set":{"done":True}})
        return jsonify({'taskUid': Uid})
    except Exception as err:
        raise ValueError("Error when updating task: ", err)


def delete(token, Uid):
    try: 
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        taskToDelete = collection.find_one({"_id": ObjectId(Uid)})
        if taskToDelete['createdByUid']!=token['id']: 
            return jsonify({'error': "Users can only delete when task is created by them."})
        collection.delete_one({"_id":taskToDelete["_id"]})
        return jsonify({'tasksAffected': 1}),200
    except Exception as err:
        raise ValueError("Error when deleting task: ", err)