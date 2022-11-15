# **MyApp API - Documentation**


 ###### [GitHub](https://github.com/yulia-samoilovich/MyApp)

| Version | Date        | Description                                                |
|---------|-------------|------------------------------------------------------------|
| 1.0     | 13-Nov-2022 | Initial documentation of an API for a task management app. |

<br>
<br>
<br>

## Index
<!-- TOC -->
* [**1. Signup**](#user-signup)

* [**2. Login**](#user-login)

* [**3. Display all users**](#display-all-users)

* [**4. Create task**](#create-task)

* [**5. Display tasks by creator's ID**](#display-tasks-by-creator-id)

* [**6. Display task by "assigned to ID"**](#display-task-by-assigned-to-id)

* [**7. Update task**](#update-task)

* [**8. Delete task**](#delete-task)
<!-- TOC -->

<br><br>


### User signup
Creates a new user account. A valid email format is necessary in the request. A UID is generated upon successful signup.

#### Request 
| Method | URL                                   |
|--------|---------------------------------------|
| POST   | http://127.0.0.1:5000/v0/users/signup |

Parameters:
`{"email":"user@gmail.com", "password": "password", "name": "User"}`

#### Response
| Status | Response                                                          |
|--------|-------------------------------------------------------------------|
| 200 OK | `{"uid": "6373014c9aadab0b3659af36"}`                             |
| 400    | {'error': 'Invalid e-mail address. Please enter a valid e-mail.'} |
| 400    | {'error': 'Email is needed in the request.}                       |
| 400    | {'error': 'Password is needed in the request.'}                   |
| 400    | {'error': 'Name is needed in the request.'}                       |
| 400    | {'error': 'There is already an user with this email.}             |
| 500    | {'error': 'Something wrong happened when creating user.'}         |

### User login
User login request. A authentication token is created upon successful login.


#### Request
| Method | URL                                  |
|--------|--------------------------------------|
| POST   | http://127.0.0.1:5000/v0/users/login |

Parameters:
`{"email": "user@gmail.com", "password": "password"}`

#### Response
| Status | Response                                                                                                                                                                                                                                                                                                                    |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK | `{"expiration": 2592000, "loggedUser": { "email": "user@gmail.com", "name": "user", "uid": "6373014c9aadab0b3659af36" }, "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXJAZ21haWwuY29tIiwiaWQiOiI2MzczMDE0YzlhYWRhYjBiMzY1OWFmMzYiLCJleHAiOjE2NzEwNzM3NjV9.DV9adDgzST4PMmqm8tUUkol2WX0tkK0KhLfNHTJz-_Q"}` |
| 400    | {'error': 'Invalid e-mail address. Please enter a valid e-mail.'}                                                                                                                                                                                                                                                           |
| 400    | {'error': 'Email is needed in the request.}                                                                                                                                                                                                                                                                                 |
| 400    | {'error': 'Password is needed in the request.'}                                                                                                                                                                                                                                                                             |
| 400    | {'error': 'Name is needed in the request.'}                                                                                                                                                                                                                                                                                 |
| 400    | {'error': 'There is already an user with this email.}                                                                                                                                                                                                                                                                       |
| 500    | {'error': 'Something wrong happened when creating user.'}                                                                                                                                                                                                                                                                   |

### Display all users
Returns a list of all users. A valid token is necessary in the request.

#### Request
| Method | URL                                |
|--------|------------------------------------|
| GET    | http://127.0.0.1:5000/v0/users/all |

No parameters

#### Response
| Status     | Response                                                                                                                                                                |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK     | `{{"email": "gabriel@gmail.com", "name": "gabriel", "uid": "6372ffeb9aadab0b3659af35"},{"email": "user@gmail.com", "name": "user", "uid": "6373014c9aadab0b3659af36"}}` |
| 400        | {'error': 'Token is missing in the request.'}                                                                                                                           |
| 401        | {'error': 'Invalid authentication token.'}                                                                                                                              |
| ValueError | {'Error upon fetching users, please try again.'}                                                                                                                        |


### Create task
Creates a new task with a task description and user id (assigned to). The request receives a token for authentication.

#### Request
| Method | URL                                       |
|--------|-------------------------------------------|
| POST   | http://127.0.0.1:5000/v0/tasks/createTask |

Parameters:
`{"description": "Some task!", "assignedToUid" : "636c72ba129ed3958fd0b74d"}`

#### Response
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

#### Request
| Method | URL                                       |
|--------|-------------------------------------------|
| GET    | http://127.0.0.1:5000/v0/tasks/createdby/ |

Parameters:
`{"Uid": "6370194a928fc3c914553e30"}`

#### Response
| Status     | Response                                                                                                                                                                                                                 |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK     | `{"assignedToName": "test", "assignedToUid": "636c72ba129ed3958fd0b74d", "createdByName": "me", "createdByUid": "6370194a928fc3c914553e30", "description": "A task!", "done": false, "uid": "637267cd1d4a686e713f70c6"}` |
| 400        | {'error': 'Token is missing in the request, please try again.'}                                                                                                                                                          |
| 401        | {'error': 'Invalid authentication token, please login again.'}                                                                                                                                                           |
| ValueError | {'error': 'Error upon fetching the tasks!'}                                                                                                                                                                              |

<br>

### Display task by "assigned to ID"
Returns a list of tasks assigned to the user that is making the request. The user must be logged in and using a valid token.


#### Request
| Method | URL                                        |
|--------|--------------------------------------------|
| GET    | http://127.0.0.1:5000/v0/tasks/assignedto/ |

No parameters

#### Response 
| Status     | Response                                                                                                                                                                                                                  |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200 OK     | `{"assignedToName": "me", "assignedToUid": "6370194a928fc3c914553e30", "createdByName": "me", "createdByUid": "6370194a928fc3c914553e30", "description": "Some task!", "done": false, "uid": "6372a0793f0ad26ff2bc8034"}` |
| 400        | {'error': 'Token is missing in the request, please try again.'}                                                                                                                                                           |
| 401        | {'error': 'Invalid authentication token, please login again.'}                                                                                                                                                            |
| ValueError | {'error': 'Error upon fetching the tasks!'}                                                                                                                                                                               |

<br>

### Update task
Updates task completion status. The update request is restricted to the user who's the task is assigned to. A valid token needs to be in the request.

#### Request 
| Method | URL                                      |
|--------|------------------------------------------|
| PATCH  | http://127.0.0.1:5000/v0/tasks/<taskUid> |

Parameters:
`{"done": true/false}`

#### Response 
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

#### Request
| Method | URL                                      |
|--------|------------------------------------------|
| DELETE | http://127.0.0.1:5000/v0/tasks/<taskUid> |

No parameters

#### Response
| Status     | Response                                                          |
|------------|-------------------------------------------------------------------|
| 200 OK     | `{"tasksAffected": 1}`                                            |
| 400        | {'error': 'Token is missing in the request.'}                     |
| 401        | {'error': 'Invalid authentication token.'}                        |
| 400        | {'error': 'The task does not exits.'}                             |
| 400        | {'error': 'Assigned user is needed in the request.'}              |
| 400        | {'error': 'This task is not created by you so you cannot delete'} |
| ValueError | {'error': 'Error deleting task.'}                                 |

