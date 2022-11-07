from flask import Flask
from database.__init__ import database
from views.user_view import user

app = Flask(__name__)

app.register_blueprint(user)

print(database)


@app.route("/")
def index():  # the entry point of the application!
    return "HOME"


if __name__ == "__main__":
    app.run()
