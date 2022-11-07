#  a class to send the information needed by the database. used inside __init__ instead of simply using the mongoClient() method.

from pymongo import MongoClient


class Database:  # removed redundant parenthesis.
    def __init__(self, dataBaseName=None, connectionString=None):  # constructor.
        if (dataBaseName is None) or (connectionString is None):  # removed redundant parenthesis. comparison to None should be if cond is None.
            raise Exception(
                "Mongo DB requires database Name and string connection!")  # raise an error in case of missing db name and String connection.
        #  the variables used within the database.
        # private attributes to restrict access to db name and connection string after they're created. the data cannot be accessed outside the Database class.
        self.__dataBaseName = dataBaseName
        self.__connectionString = connectionString
        self.__dbConnection = None  # receiving the connection to the db.
        self.__dataBase = None  # the instance of the database itself.

    @property
    def dataBase(self):  # creating property get to allow access to private attributes.
        return self.__dataBase

    @property
    def dbConnection(self):
        return self.__dbConnection

    def connect(self) -> bool:  # indicating method return type for better readability.
        try:
            self.__dbConnection = MongoClient(
                self.__connectionString)  # populating the connection. saving the connection string in __dbConnection attribute.
            dbName = str(self.__dataBaseName)  # to convert any dataBaseName input to a string.
            self.__dataBase = self.__dbConnection[dbName]  # the database instance receives the dbConnection in dbName.
            return True
        except Exception as err:
            print("MongoDB connection error!", err)
            return False
