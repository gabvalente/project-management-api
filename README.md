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
* * [**Request**](#request)
* * [**Response**](#response)
* 
* [**2. Display tasks by creator's ID**](#display-tasks-by-creator-id)
* * [**Request**](#request)
* * [**Response**](#response)
* 
* [**3. Display task by assigned ID**](#display-task-by-assigned-id)
* * [**Request**](#request)
* * [**Response**](#response)
* 
* [**4. Update task**](#update-task)
* * [**Request**](#request)
* * [**Response**](#response)
* 
* [**5. Delete task**](#delete-task)
* * [**Request**](#request)
* * [**Response**](#response)
<!-- TOC -->

<br><br>

### Create task
Creates a new task with a task description and user id (assigned to). The request receives a token for authentication.

#### Request

| Method | URL                                       |
|--------|-------------------------------------------|
| POST   | http://127.0.0.1:5000/v0/tasks/createTask |

Body:
`{
    "description": "Some task!",
    "assignedToUid" : "636c72ba129ed3958fd0b74d"
}`

#### Response

| Status     | Response                                                    |
|------------|-------------------------------------------------------------|
| 200 OK     | "uid": "637267cd1d4a686e713f70c6"                           |
| 400        | {'error': 'Token is missing in the request.'}               |
| 401        | {'error': 'Invalid authentication token.'}                  |
| 400        | {'error': 'Description is needed in the request.'}          |
| 400        | {'error': 'Assigned user is needed in the request.'}        |
| 400        | {'error': 'The user who was assigned the task is invalid.'} |
| ValueError | {'error': 'Error creating task.'}                           |

<br>

### Display tasks by creator ID
Returns a list of tasks created based on the creator's ID. A valid token needs to be in the request.

#### Request
| Method | URL                                       |
|--------|-------------------------------------------|
| GET    | http://127.0.0.1:5000/v0/tasks/createdby/ |

Body:
`{
    "Uid": "6370194a928fc3c914553e30"
}`

#### Response

| Status     | Response                                                                                                                                                                                                                    |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK     | `{"assignedToName": "test", "assignedToUid": "636c72ba129ed3958fd0b74d", "createdByName": "me", "createdByUid": "6370194a928fc3c914553e30", "description": "Some task!", "done": false, "uid": "637267cd1d4a686e713f70c6"}` |
| 400        | {'error': 'Token is missing in the request.'}                                                                                                                                                                               |
| 401        | {'error': 'Invalid authentication token.'}                                                                                                                                                                                  |
| ValueError | {'error': 'Error fetching task.'}                                                                                                                                                                                           |

<br>

### Display task by assigned ID
Returns a list of tasks assigned to the user that is making the request. The user must be logged in and using a valid token.

Body:
`{
    "Uid": "6370194a928fc3c914553e30"
}`

#### Request
| Method | URL                                        |
|--------|--------------------------------------------|
| GET    | http://127.0.0.1:5000/v0/tasks/assignedto/ |

#### Response

| Status     | Response                                      |
|------------|-----------------------------------------------|
| 200 OK     | "uid": "637267cd1d4a686e713f70c6"             |
| 400        | {'error': 'Token is missing in the request.'} |
| 401        | {'error': 'Invalid authentication token.'}    |
| ValueError | {'error': 'Error fetching task.'}             |

<br>

### Update task
Updates task completion status. The update request is restricted to the user who's the task is assigned to. A valid token needs to be in the request.

#### Request
| Method | URL                                      |
|--------|------------------------------------------|
| PATCH  | http://127.0.0.1:5000/v0/tasks/<taskUid> |

#### Response

| Status     | Response                                                           |
|------------|--------------------------------------------------------------------|
| 200 OK     |                                                                    |
| 400        | {'error': 'Token is missing in the request.'}                      |
| 401        | {'error': 'Invalid authentication token.'}                         |
| 400        | {'error': 'Done is needed in the request.'}                        |
| 400        | {'error': 'The task does not exits.'}                              |
| 400        | {'error': 'This task is not assigned to you so you cannot update'} |
| ValueError | {'error': 'Error updating task.'}                                  |

<br>

### Delete task
Deletes a task from the database. The delete request is restricted to the user who created the task. A valid token needs to be in the request.

#### Request
| Method | URL                                      |
|--------|------------------------------------------|
| DELETE | http://127.0.0.1:5000/v0/tasks/<taskUid> |

#### Response

| Status     | Response                                                          |
|------------|-------------------------------------------------------------------|
| 200 OK     | "uid": "637267cd1d4a686e713f70c6"                                 |
| 400        | {'error': 'Token is missing in the request.'}                     |
| 401        | {'error': 'Invalid authentication token.'}                        |
| 400        | {'error': 'The task does not exits.'}                             |
| 400        | {'error': 'Assigned user is needed in the request.'}              |
| 400        | {'error': 'This task is not created by you so you cannot delete'} |
| ValueError | {'error': 'Error deleting task.'}                                 |

