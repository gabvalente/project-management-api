from flask import Flask
from database.__init__ import database
from views.user_view import user
from views.task_view import task

app = Flask(__name__)

app.register_blueprint(user)

app.register_blueprint(task)

print(database)

@app.route("/")
def index():
    return "HOME"

if __name__ == "__main__":
    app.run()
