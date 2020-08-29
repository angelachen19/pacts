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
    user = User.query.filter_by(email=user_email).first()
    if (user.password != user_password):
        return None
    return user.serialize()


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
    return group.serialize()


def remove_user_from_group(user_id, group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    group.users.remove(user)
    db.session.commit()
    return group.serialize()

def update_group():
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    group.name = body.get("name", group.name)
    group.description = body.get("description", group.description)
    db.session.commit()
    return group.serialize()

def delete_group(group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    db.session.delete(groups)
    db.session.commit()
    return group.serialize()

# def get_messages_in_group(group_id):
#     group = group.query.filter_by(id=group_id).first()
#     if group is None:
#         return None
#     return []########todo



######################################################################################################
#Activity
#This stuff is all on the dev side
def get_all_activities():
    return [w.serialize() for w in Activity.query.all()]

def get_activity_by_id():
    activity = Activity.query.filter_by(id=group_id).first()
    if group is None:
        return None
    return group.serialize()

def create_activity():
    activity = Activity.query.filter_by(id=user_id).first()
    if user is None:
        return None
    new_group = Group(
        name=name,
        organizer=organizer_id #should is save id? or user itself?
    )
    db.session.add(new_group)
    db.session.commit()
    return new_group.serialize()

def update_activity():
    activity = Activity.query.filter_by(id=group_id).first()
    if activity is None:
        return None
    activity.name = body.get("name", activity.name)
    activity.timeofday = body.get("timeofday", activity.timeofday)
    activity.weather = body.get("weather", activity.weather)
    activity.minnumppl = body.get("minnumppl", activity.minnumppl)
    activity.maxnumppl = body.get("maxnumppl", activity.maxnumppl)
    activity.location = body.get("location", activity.location)
    activity.description = body.get("description", activity.descriiption)
    db.session.commit()
    return group.serialize()

def delete_activity():
    activity = Activity.query.filter_by(id=activity_id).first()
    if activity is None:
        return None
    db.session.delete(activity)
    db.session.commit()
    return group.serialize()

######################################################################################################
#Message
# def get_all_messages():

# def get_message_by_id():

# def get_messages_in_group(group_id): #need polls here too...should id do this in db?

# def create_message(sender_id, content, group_id):

# def delete_message_by_id(message_id):


######################################################################################################
#Poll
# def get_all_polls():

# def get_poll_by_id(poll_id)

# def get_poll_in_group(group_id):

# def create_poll(group_id):

# def change_poll_status(poll_id):

######################################################################################################
#Event
def get_all_events():
    return [w.serialize() for w in Event.query.all()]

def get_event_by_id(event_id)
    event = Event.query.filter_by(id=Event_id).first()
    if event is None:
        return None
    return event.serialize()

def get_events_in_group(group_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    return [m.serialize() for m in group.messages]

def create_event(group_id, organizer_id, location, time):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    new_event = event(
        name=name,
        organizer=organizer_id, #should is save id? or user itself?
        location = location,
        time = time
    )
    db.session.add(new_event)
    db.session.commit()
    return new_event.serialize()

def delete_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    db.session.delete(event)
    db.session.commit()
    return event.serialize()
