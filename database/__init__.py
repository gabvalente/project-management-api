from pymongo import MongoClient
from .db import Database
import app_config as config  # importing string connection and db name.

# database = MongoClient()  - bad practice, exposes sensitive data.

database = Database(connectionString=config.CONST_MONGO_URL, dataBaseName=config.CONST_DATABASE)  # creating a new instance of Database class inside the database variable.
database.connect()

