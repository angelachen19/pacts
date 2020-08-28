from time import time, ctime
from db import db, User, Group, Activiity, Message, Poll, Event

#learn oauth?
#todo: 


######################################################################################################
#User
def get_all_users():
    return [u.serialize() for u in User.query.all()]

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()

def create_user():
    new_user = User(
        name = name,
        email = email,
        year = year,
        password = password
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def update_user_by_id(user_id, body):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    user.name = body.get("name", user.name)
    user.email = body.get("email", user.email)
    user.year = body.get("year", user.year)
    user.password = body.get("password", user.password)
    user.pfp = body.get("pfp", user.pfp)
    db.session.commit()
    return user.serialize()

def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def log_in(user_email, user_password):

######################################################################################################
#Group
def get_all_groups():
    return [w.serialize() for w in Group.query.all()]

def get_group_by_id(group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    return group.serialize()

def create_group(name=None, organizer_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    new_group = Group(
        name=name,
        organizer=organizer_id #should is save id? or user itself?
    )
    db.session.add(new_group)
    db.session.commit()
    return new_group.serialize()

def add_user_to_group(user_id, group_id):
     group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    group.users.append(user)
    db.session.commit()
    return channel.serialize()


def remove_user_from_group(user_id, group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    group.users.remove(user)
    db.session.commit()
    return channel.serialize()

def update_group():
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    channel.name = body.get("name", channel.name)
    channel.description = body.get("description", channel.description)
    db.session.commit()
    return channel.serialize()

def delete_group(group_id):

def get_messages_in_group(group_id):
    group = group.query.filter_by(id=channel_id).first()
    if group is None:
        return None
    return 



######################################################################################################
#Activity
def get_all_activities():

def get_activity_by_id():

def update_activity():

def delete_activity():

######################################################################################################
#Message
def get_all_messages():

def get_message_by_id():

def get_messages_in_group(group_id): #need polls here too...should id do this in db?

def create_message(sender_id, content, group_id):

def delete_message_by_id(message_id):


######################################################################################################
#Poll
def get_all_polls():

def get_poll_by_id(poll_id)

def get_poll_in_group(group_id):

def create_poll(group_id):


######################################################################################################
#Event
def get_all_events():

def get_event_by_id(event_id)

def get_events_in_group(group_id):

def create_event(group_id):

def delete_event(event_id):


