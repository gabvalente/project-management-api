# **MyApp API - Documentation**
##### Task Management Application

 ###### [GitHub](https://github.com/yulia-samoilovich/MyApp)

| Version | Date        |  Description  |
|---------|-------------|---------------|
| 1.0     | 13-Nov-2022 | Initial draft |

<br>

###### Team members: 
* Matthew Bernett
* Hyemi Park
* Yulia Samoilovich
* Thi Hau Vu
* Maria Agudelo
* Gabriel Valente

<br>
<br>

## Index
<!-- TOC -->
* [**1. Create task**](#create-task)

* [**2. Display tasks by creator's ID**](#display-tasks-by-creator-id)

* [**3. Display task by "assigned to ID"**](#display-task-by-assigned-to-id)

* [**4. Update task**](#update-task)

* [**5. Delete task**](#delete-task)
<!-- TOC -->

<br><br>

### Create task
Creates a new task with a task description and user id (assigned to). The request receives a token for authentication.

#### Request (create)
| Method | URL                                       |
|--------|-------------------------------------------|
| POST   | http://127.0.0.1:5000/v0/tasks/createTask |

Parameters:
`{"description": "Some task!", "assignedToUid" : "636c72ba129ed3958fd0b74d"}`

#### Response (create)
| Status     | Response                                                        |
|------------|-----------------------------------------------------------------|
| 200 OK     | `{"uid": "637267cd1d4a686e713f70c6"}`                           |
| 400        | {'error': 'Token is missing in the request, please try again.'} |
| 401        | {'error': 'Invalid authentication token, please login again.'}  |
| 400        | {'error': 'Description is needed in the request.'}              |
| 400        | {'error': 'Assigned user is needed in the request.'}            |
| 400        | {'error': 'Task assigned to an invalid user, please try again.} |
| ValueError | {'error': 'Error upon creating the task!'}                      |

<br>

### Display tasks by creator ID
Returns a list of all tasks based on the creator's ID. A valid token is necessary in the request.

#### Request (display by UID)
| Method | URL                                       |
|--------|-------------------------------------------|
| GET    | http://127.0.0.1:5000/v0/tasks/createdby/ |

Parameters:
`{"Uid": "6370194a928fc3c914553e30"}`

#### Response (display by UID)
| Status     | Response                                                                                                                                                                                                                 |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK     | `{"assignedToName": "test", "assignedToUid": "636c72ba129ed3958fd0b74d", "createdByName": "me", "createdByUid": "6370194a928fc3c914553e30", "description": "A task!", "done": false, "uid": "637267cd1d4a686e713f70c6"}` |
| 400        | {'error': 'Token is missing in the request, please try again.'}                                                                                                                                                          |
| 401        | {'error': 'Invalid authentication token, please login again.'}                                                                                                                                                           |
| ValueError | {'error': 'Error upon fetching the tasks!'}                                                                                                                                                                              |

<br>

### Display task by "assigned to ID"
Returns a list of tasks assigned to the user that is making the request. The user must be logged in and using a valid token.


#### Request (display by assigned to ID)
| Method | URL                                        |
|--------|--------------------------------------------|
| GET    | http://127.0.0.1:5000/v0/tasks/assignedto/ |

No parameters

#### Response (display by assigned to ID)
| Status     | Response                                                                                                                                                                                                                  |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK     | `{"assignedToName": "me", "assignedToUid": "6370194a928fc3c914553e30", "createdByName": "me", "createdByUid": "6370194a928fc3c914553e30", "description": "Some task!", "done": false, "uid": "6372a0793f0ad26ff2bc8034"}` |
| 400        | {'error': 'Token is missing in the request, please try again.'}                                                                                                                                                           |
| 401        | {'error': 'Invalid authentication token, please login again.'}                                                                                                                                                            |
| ValueError | {'error': 'Error upon fetching the tasks!'}                                                                                                                                                                               |

<br>

### Update task
Updates task completion status. The update request is restricted to the user who's the task is assigned to. A valid token needs to be in the request.

#### Request (update)
| Method | URL                                      |
|--------|------------------------------------------|
| PATCH  | http://127.0.0.1:5000/v0/tasks/<taskUid> |

Parameters:
`{"done": true/false}`

#### Response (update)
| Status     | Response                                                                                     |
|------------|----------------------------------------------------------------------------------------------|
| 200 OK     | `{"taskUid": "6372a2a13f0ad26ff2bc8036"}`                                                    |
| 400        | {'error': 'Token is missing in the request, please try again.'}                              |
| 401        | {'error': 'Invalid authentication token, please login again.'}                               |
| 400        | {'error': '"Done" status not found in the request.'}                                         |
| 400        | {'error': 'Task not found.'}                                                                 |
| 400        | {'error': 'The task status can only be changed by the user to who the task is assigned to.'} |
| ValueError | {'error': 'Error upon updating task!'}                                                       |

<br>

### Delete task
Deletes a task from the database. The delete request is restricted to the user who created the task. A valid token needs to be in the request.

#### Request (delete)
| Method | URL                                      |
|--------|------------------------------------------|
| DELETE | http://127.0.0.1:5000/v0/tasks/<taskUid> |

No parameters

#### Response (delete)
| Status     | Response                                                          |
|------------|-------------------------------------------------------------------|
| 200 OK     | `{"tasksAffected": 1}`                                            |
| 400        | {'error': 'Token is missing in the request.'}                     |
| 401        | {'error': 'Invalid authentication token.'}                        |
| 400        | {'error': 'The task does not exits.'}                             |
| 400        | {'error': 'Assigned user is needed in the request.'}              |
| 400        | {'error': 'This task is not created by you so you cannot delete'} |
| ValueError | {'error': 'Error deleting task.'}                                 |

