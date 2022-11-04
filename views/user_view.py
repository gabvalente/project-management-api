from flask import Blueprint
from database.__init__ import database
from models.user_model import User

user = Blueprint("user", __name__)

@user.route("/v0/user/", methods=["POST"])
def create():
    return "POST METHOD"

@user.route("/v0/user/", methods=["GET"])
def fetch():
    myUser = User()
    myUser.name = "Yulia"
    myUser.email = "yulia@email.com"
    myUser.password = "12345"

    database["LS3"]["user"].insert_one(myUser.__dict__)
    return "User was added"