from flask_sqlalchemy import SQLAlchemy
from time import time, ctime
db = SQLAlchemy()

#assoc tables: user to groups, user to events
association_table_usergrp = db.Table('association_usergrp', db.Model.metadata,
    db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

association_table_attevt = db.Table('association_userevt', db.Model.metadata,
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

association_table_nattevt = db.Table('association_userevt', db.Model.metadata,
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

    #many: db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #one: db.relationship('Message', cascade='delete')

    #todo: poll stuff
    #todo: return messages and polls in order in groups

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String, nullable=False)
    pfp = db.Column(db.String, nullable=False)
    groups = db.relationship('Group', secondary=association_table_usergrp, back_populates='members')#many to many with 'groups'
    events = db.relationship('Event', secondary=association_table_nattevt, back_populates='attending')#many to many with 'events'
    #nevents = events they didnt attend, here for the table but never seriialized
    nevents = db.relationship('Event', secondary=association_table_nattevt, back_populates='notattending')#many to many with 'events'
    # messages = db.relationship('Message', cascade='delete') #relationship one (user) to many (dms)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.email = kwargs.get('email', '')
        self.year = kwargs.get('year', '')
        self.password = kwargs.get('password', '')
        self.pfp = kwargs.get('pfp', '')

    def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'year':self.year,
            'pfp':self.pfp,
            'groups':[a.serialize_name() for a in self.groups],
            'events':[s.serialize() for s in self.events]
        }

    def serialize_name(self):
        return{
            'id':self.id,
            'name':self.name
        }


class Group(db.Model):
    __tablename__='group'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = True) #name of group
    organizer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    members = ('User', secondary=association_table_usergrp, back_populates='groups')
    events = db.relationship('Event', cascade='delete')#one to many with 'events'
    # messages = db.relationship('Message', cascade='delete')#one to many with 'messages'
    polls = db.relationship('Poll', cascade='delete')#one to  many with 'polls'

     def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')

     def serialize_name(self):
        return{
            'id':self.id,
            'name': self.name
        }

     def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'organizer': [s.serialize_name() for s in self.user] ,
            'members':  [s.serialize_name() for s in self.members],
            'events': [s.serialize_name() for s in self.events] ,
            # 'messages':  #messages thing
            'polls': #polls thing
        }

class Activity(db.Model):
    __tablename__='activity'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String, nullable = False)
    category = db.Column (db.String, nullable = False)
    timeofday = db.Column (db.String, nullable = True)
    weather =  db.Column (db.String, nullable = True)
    minnumppl = db.Column (db.Integer, nullable = True)
    maxnumppl = db.Column (db.Integer, nullable = True)
    location = db.Column (db.String, nullable = False)
    description = db.Column (db.String, nullable = False)

    def __init__(self, **kwargs):
        self.category = kwargs.get('category', '')
        self.timeofday = kwargs.get('timeofday', '')
        self.weather = kwargs.get('weather','')
        self.minnumppl = kwargs.get('mininumppl', '')
        self.maxnumppl = kwargs.get('maxnumppl','')
        self.location = kwargs.get('location', '')
        self.description = kwargs.get('description','')

    def serialize(self):
        return{
            'id':self.id,

        }

# class Message(db.Model):
#     __tablename__='message'
#     id = db.Column(db.Integer, primary_key = True)
#     sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     content = db.Column (db.String, nullable = False)
#     timestamp = db.Column (db.String, nullable = False)
#     group = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #many to one with group

#     def __init__(self, **kwargs):
#         self.sender = kwargs.get('sender', '')
#         self.content = kwargs.get('content', '')
#         self.timestamp = ctime()
#         self.channel = kwargs.get('channel', '')

#     def serialize(self):
#         sender = User.query.filter_by(id=self.sender).first()
#         if sender is None:
#             return None
#         group = Group.query.filter_by(id=self.group).first()
#         if group is None:
#             return None
#         return{
#             'id':self.id,
#             'sender':sender.serialize_name(),
#             'content':self.content,
#             'timestamp':self.timestamp,
#             'group':group.serialize_name()
#         }

#Organizer will choose a set day and others in pact will vote on time of day
#json.dumps turns json into String
#json.loads turns string into json
# Poll 1 is the initial event poll: voting on category, date and time
class Poll1(db.Model):
    __tablename__='poll1'
    id = db.Column(db.Integer, primary_key = True)
    active = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    timestamp =  db.Column(db.String,  nullable=False)
    eventday = db.Column(db.String, nullable=False)
    choice1 = db.Column(db.String, nullable=False) #Category of activity
    answer1 = db.Column(db.String, nullable=True)#json map for writing user:answer
    choice2 = db.Column(db.String, nullable=False) # Time of day
    answer2 = db.Column(db.String, nullable=True)

    def __init__(self, **kwargs):
        self.active = kwargs.get('active','')
        self.timestamp = ctime()
        self.eventday = kwargs.get('eventday', '')
        self.group = kwargs.get('group', '')
        self.choice1 = json.dumps([])#array
        self.answer1 = json.dumps({})#dictionary
        self.choice2 = json.dumps([])#array
        self.answer2 = json.dumps({})#dictionary

    def serialize(self):
        group = Group.query.filter_by(id=self.group).first()
        return{
            'id':self.id,
            'question':self.question,
            'timestamp':self.timestamp,
            'group': group.serialize_name(),
            'choice1': json.loads(self.choice1),
            'answer1': json.loads(self.answer1),
            'choice2': json.loads(self.choice2),
            'answer2': json.loads(self.answer2)
        }

# Poll 2 is the second poll for an event: voting on the actual event and saying yes/no to attending
class Poll2(db.Model):
    __tablename__='poll2'
    id = db.Column(db.Integer, primary_key = True)
    active = db.Column(db.Boolean, nullable=False)
    poll1 = db.Column(db.Integer, db.ForeignKey('poll1.id'), nullable=False)
    group = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    timestamp =  db.Column(db.String,  nullable=False)
    eventtime = db.Column(db.String, nullable=False) #actual time of event
    choices = db.Column(db.String, nullable=False)
    answers = db.Column(db.String, nullable=True)#json map for writing user:answer

    def __init__(self, **kwargs):
        self.question = kwargs.get('question', '')
        self.poll1 = kwargs.get('poll1', '')
        self.active = kwargs.get('active','')
        self.group = kwargs.get('group', '')
        self.timestamp = ctime()
        self.eventtime = kwargs.get('eventtime', '')
        self.choices = json.dumps([])#array
        self.answers = json.dumps({})#dictionary

    def serialize(self):
        group = Group.query.filter_by(id=self.group).first()
        return{
            'id':self.id,
            'poll1': self.poll1,
            'question':self.question,
            'timestamp':self.timestamp,
            'group': group.serialize_name(),
            'choices': json.loads(self.choices),
            'answers': json.loads(self.answers)
        }

class Event(db.Model):
    __tablename__='event'
    id = db.Column(db.Integer, primary_key = True)
    active = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    organizer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    location =  db.Column(db.String, nullable=False) #address, or modality
    time = db.Column(db.String, nullable=False)
    attending = ('User', secondary=association_table_attevt, back_populates='events')
    notattending = ('User', secondary=association_table_nattevt, back_populates='events')

    def __init__(self, **kwargs):
        self.active = True
        self.group = kwargs.get('group', '')
        self.organizer = kwargs.get('organizer','')
        self.name = kwargs.get('name','')
        self.location = kwargs.get('location,','')
        self.time =  kwargs.get('time', '')

    def serialize(self):
        organizer = User.query.filter_by(id=self.organizer).first()
        group = Group.query.filter_by(id=self.group).first()
        if organizer is None or group is None:
            return None
        return{
            'id':self.id,
            'active':self.active,
            'group':group.serialize_name(),
            'organizer':organizer.serialize_name(),
            'name':self.name,
            'location': self,location,
            'time': self.time,
            'attending': [s.serialize_name() for s in self.attending],
            'notattending': [s.serialize_name() for s in self.notattending]
        }

    def serialize_for_group(self):
        organizer = User.query.filter_by(id=self.organizer).first()
        if organizer is None:
            return None
        return{
            'id':self.id,
            'active':self.active,
            'organizer':organizer.serialize_name(),
            'name':self.name,
            'location': self,location,
            'time': self.time
        }
