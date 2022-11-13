from flask import jsonify
from models.task_model import Task
from database.__init__ import database
import app_config as config
from bson.objectid import ObjectId


def get_username_by_uid(uid):
    collection = database.dataBase[config.CONST_USER_COLLECTION]
    user_info = collection.find_one({"_id": ObjectId(uid)})
    return user_info['name']


def create_task(user_information, task_information):
    new_task = None
    try:
        new_task = Task()
        new_task.description = task_information['description']
        new_task.createdByUid = user_information['id']
        new_task.createdByName = get_username_by_uid(user_information['id'])
        new_task.assignedToUid = task_information['assignedToUid']
        new_task.assignedToName = get_username_by_uid(task_information['assignedToUid'])

        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        created_task = collection.insert_one(new_task.__dict__)
        return created_task
    except Exception as err:
        raise ValueError('Error on creating task: ', err)


def fetch_created_task(uid):
    try:
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        created_tasks = []

        for task in collection.find():
            if str(task['createdByUid']) == str(uid):
                current_task = {}
                current_task.update({'uid': str(task['_id'])})
                current_task.update({'description': task['description']})
                current_task.update({'createdByUid': str(task['createdByUid'])})
                current_task.update({'createdByName': task['createdByName']})
                current_task.update({'assignedToUid': str(task['assignedToUid'])})
                current_task.update({'assignedToName': task['assignedToName']})
                current_task.update({'done': task['done']})
                created_tasks.append(current_task)

        return created_tasks

    except Exception as err:
        raise ValueError("Error when trying to fetch tasks: ", err)


def fetch_assigned_task(Uid):
    try:
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        created_tasks = []

        for task in collection.find():
            if str(task['assignedToUid']) == str(Uid):
                current_task = {}
                current_task.update({'uid': str(task['_id'])})
                current_task.update({'description': task['description']})
                current_task.update({'createdByUid': task['createdByUid']})
                current_task.update({'createdByName': task['createdByName']})
                current_task.update({'assignedToUid': task['assignedToUid']})
                current_task.update({'assignedToName': task['assignedToName']})
                current_task.update({'done': task['done']})
                created_tasks.append(current_task)
        return created_tasks
    except Exception as err:
        raise ValueError("Error when trying to fetch tasks: ", err)


def checking_task_in_list(task_list, task_uid):
    count = 0
    for task in task_list:
        if str(task['uid']) == str(task_uid):
            count = count + 1
    if count == 0:
        return 0


def update_task(user_information, uid):
    try:
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        task_to_update = collection.find_one({"_id": ObjectId(uid)})
        collection.update_one({"_id": task_to_update["_id"]}, {
            "$set": {"done": user_information["done"]}})
        return jsonify({'taskUid': uid})
    except Exception as err:
        raise ValueError("Error when updating task: ", err)


def delete(uid):
    try:
        collection = database.dataBase[config.CONST_TASK_COLLECTION]
        task_to_delete = collection.find_one({"_id": ObjectId(uid)})
        collection.delete_one({"_id": task_to_delete["_id"]})
        return jsonify({'tasksAffected': 1}), 200
    except Exception as err:
        raise ValueError("Error when deleting task: ", err)
