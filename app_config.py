# saving constant information to be used across program.

CONST_MONGO_URL = "mongodb+srv://pythonls3:vMdBTmZFeylsNJKX@cluster0.7s4my0s.mongodb.net/?retryWrites=true&w=majority"  # the url used to connect to the db.
CONST_DATABASE = "LS3"  # the database name.
CONST_USER_COLLECTION = "users"  # one of the collections. Collections in mongodb = tables in SQL.

TOKEN_SECRET = "iosandpython"
JWT_EXPIRATION = 86400*30