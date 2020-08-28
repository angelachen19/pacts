import json
from flask import Flask, request
import dao
import os
from db import db, User, Group, Activiity, Message, Poll, Event

app = Flask(__name__)
db_filename = "slack.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code
######################################################################################################

@app.route('/users/', methods=['GET'])
def get_all_users():
    return success_response(dao.get_all_users())

@app.route('/users/<int:user_id>/', methods=['GET'])
def








######################################################################################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
