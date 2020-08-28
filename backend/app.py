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
#users
#get all users
@app.route('/users/', methods=['GET'])
def get_all_users():
    return success_response(dao.get_all_users())
#get user by id
@app.route('/users/<int:user_id>/', methods=['GET'])
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

#create user
@app.route('/users/', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        name=body.get('name'),
        email=body.get('email'),
        year = body.get('year'),
        password = body.get('password')
    )
    return success_response(user)
#update user by id
@app.route('/users/', methods=['POST'])
def update_user_by_id(user_id):
    body = json.loads(request.data)
    user = dao.update_user_by_id(user_id, body)
    if user is None:
         return failure_response("User not found!")
    return success_response(user)

#delete user@
@app.route('/users/<int:user_id>/', methods=['DELETE'])
def update_user_by_id(user_id):
    body = json.loads(request.data)
    user = dao.update_user_by_id(user_id, body)
    if user is None:
         return failure_response("User not found!")
    return success_response(user)

######################################################################################################
#Group

#get all groups
@app.route('/groups/', methods=['GET'])
def get_all_users():
    return success_response(dao.get_all_users())
#get group by id
@app.route('/groups/<int:group_id>/', methods=['GET'])
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)
#create group
@app.route('/groups/', methods=['POST'])

#add user to group
@app.route('/groups/<int:group_id>/add/', methods=['POST'])
def add_user_to_group(user_id, group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    group.users.append(user)
    db.session.commit()
    return channel.serialize()
    
#remove user from groups

#update group

#delete group


######################################################################################################
#Activity

#get all activities
#get activities by id
#create activity
#update activity
#delete activity

######################################################################################################
#Poll

######################################################################################################
#Event

#get all events
#get event by id
#get events in group
#create event
#delete event




######################################################################################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

