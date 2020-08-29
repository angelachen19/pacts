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

def create_group(name=None, user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    new_group = Group(
        name=name,
        organizer=user_id #should is save id? or user itself?
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

def update_group(group_id, body):
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
    db.session.delete(group)
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

def get_activity_by_id(activity_id):
    activity = Activity.query.filter_by(id=activity_id).first()
    if activity is None:
        return None
    return activity.serialize()

def create_activity(name, category, timeofday, weather, minnumppl, maxnumppl, location, description):
    activity = Activity.query.filter_by(id=activity_id).first()
    new_activity = Activity(
        name=name,
        category=category,
        timeofday=timeofday,
        weather=weather,
        minnumppl=minnumppl,
        maxnumppl=maxnumppl,
        location=location,
        description=description
    )
    db.session.add(new_activity)
    db.session.commit()
    return new_activity.serialize()

def update_activity(activity_id, body):
    activity = Activity.query.filter_by(id=activity_id).first()
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
    return activity.serialize()

def delete_activity(activity_id):
    activity = Activity.query.filter_by(id=activity_id).first()
    if activity is None:
        return None
    db.session.delete(activity)
    db.session.commit()
    return activity.serialize()

######################################################################################################
#Message
# def get_all_messages():

# def get_message_by_id():

# def get_messages_in_group(group_id): #need polls here too...should id do this in db?

# def create_message(sender_id, content, group_id):

# def delete_message_by_id(message_id):


######################################################################################################
#Poll 1
def get_all_poll1s():
    return [p.serialize() for p in Poll1.query.all()]

def get_poll1_by_id(poll1_id):
    poll1 = Poll1.query.filter_by(id=poll1_id).first()
    if poll1 is None:
        return None
    return poll1.serialize()

def get_poll1s_in_group(group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    return [p.serialize() for p in group.poll1s]

def create_poll1(group_id, eventday):
        group = Group.query.filter_by(id=group_id).first()
        if group is None:
            return None
        new_poll1 = poll1(
            active=True,
            eventday=eventday,
            group=group_id,
            choice1=json.dumps(["Virtual", "Outdoors", "School Event", "Dining"]),
            choice2=json.dumps(["Morning", "Afternoon", "Evening"]),
        )
        db.session.add(new_poll1)
        db.session.commit()
        return new_poll1.serialize()

def create_poll2(group_id, poll1_id, eventtime):
        group = Group.query.filter_by(id=group_id).first()
        poll1 = Poll1.query.filter_by(id=poll1_id).first()
        if group is None:
            return None
        if poll1 is None:
            return None
        new_poll2 = poll2(
            active=True,
            poll1=poll1_id,
            eventtime=eventtime,
            group=group_id,
            choices=json.dumps([
            "Hiking with Touchdown",
            "Apple Picking",
            "Paddling at Cayuga Lake",
            "Picnic on the Slope",
            "Visit the Sagan Planet Walk"]), #given more time, we would actually suggest events based on polls
        )
        db.session.add(new_poll2)
        db.session.commit()
        return new_poll2.serialize()

def update_poll1(poll1_id, body):
    poll1 = Poll1.query.filter_by(id=poll1_id).first()
    if poll1 is None:
        return None
    poll1.answer1 = body.get("name", activity.name
    db.session.commit()
    return activity.serialize()


######################################################################################################
#Event
def get_all_events():
    return [w.serialize() for w in Event.query.all()]

def get_event_by_id(event_id):
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return None
    return event.serialize()

def get_events_in_group(group_id):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    return [m.serialize() for m in group.events]

def create_event(group_id, organizer_id, location, time):
    group = Group.query.filter_by(id=group_id).first()
    if group is None:
        return None
    new_event = event(
        name=name,
        group=group_id,
        organizer=organizer_id, #should is save id? or user itself?
        location=location,
        time=time
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

def add_vote(event_id, user_id):
    event = Event.query.filter-by(id=event_id).first()
    user = User.query.filter_by(id=user_id).first()
    if user is None or event is None:
        return None
    event.attending.append(user)
    db.session.commit()
    return event.serialize()

def remote_vote(event_id, user_id):
    event = Event.query.filter-by(id=event_id).first()
    user = User.query.filter_by(id=user_id).first()
    if user is None or event is None:
        return None
    event.notattending.append(user)
    db.session.commit()
    return event.serialize()
