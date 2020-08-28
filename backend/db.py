from flask_sqlalchemy import SQLAlchemy
from time import time, ctime
db = SQLAlchemy()

#assoc tables: user to groups, user to events
association_table_usergrp = db.Table('association_usergrp', db.Model.metadata,
    db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

association_table_userevt = db.Table('association_userevt', db.Model.metadata,
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
    events = db.relationship('Event', secondary=association_table_userevt, back_populates='members')#many to many with 'events'
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
    messages = db.relationship('Message', cascade='delete')#one to many with 'messages'
    polls = db.relationship('Poll', cascade='delete')#one to  many with 'polls'

     def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')

     def serialize_name(self):
        return{
            'id':self.id,
        }

     def serialize(self):
        return{
            'id':self.id,
            'name':self.name,
            'organizer': [s.serialize_name() for s in self.user] ,
            'members':  [s.serialize_name() for s in self.members],
            'events': [s.serialize_name() for s in self.members] ,
            'messages':  #messages thing
            'polls': #polls thing
        }

class Activity(db.Model):
    __tablename__='activity'
    id = db.Column(db.Integer, primary_key = True)
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

class Poll(db.Model):
    __tablename__='poll'
    id = db.Column(db.Integer, primary_key = True)
    active = db.Column(db.Boolean, nullable=False)
    question = db.Column(db.String, nullable=False)
    timestamp =  db.Column(db.String,  nullable=False)
    expiretime = db.Column(db.String, nullable=False)
    choices = db.Column(db.JSON, nullable=False) #db.json?!?! bwahahaha
    answers = #json map for writing user:answer

    def __init__(self, **kwargs):
        self.question = kwargs.get('question', '')
        self.active = kwargs.get('active','')
        self.timestamp = ctime()
        self.expiretime = kwargs.get('expiretime','')
        self.choices = #parse the json?!
        self.answers = #parse the json?!
        
    def serialize(self):
        return{ 
            'id':self.id,
            'question':self.question,
            'timestamp':self.timestamp,
            'expiretime':self.expiretime,
            'choices': #serialze choices?
            'answers': #serialize answers?
             #count amount of votes for each choice?
        }

class Event(db.Model):
    __tablename__='event'
    id = db.Column(db.Integer, primary_key = True)
    active = db.Column(db.Boolean, nullable=False)
    organizer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    location =  db.Column(db.String, nullable=False) #address, or modality
    time = db.Column(db.String, nullable=False)
    members = ('User', secondary=association_table_userevt, back_populates='events')
    
    def __init__(self, **kwargs):
        self.active = True
        self.organizer = kwargs.get('organizer','')
        self.name = kwargs.get('name','')
        self.location = kwargs.get('location,','')
        self.time =  kwargs.get('time', '')
    
    def serialize(self):
        return{ 
            'id':self.id,
            'active':self.active,
            'organizer':self.organizer,
            'name':self.name,
            'location': self,location,
            'time': self.time
            'members': [s.serialize_name() for s in self.members]
        }

    def serialize_for_group(self):
        return{
            'id':self.id,
            'active':self.active,
            'organizer':self.organizer,
            'name':self.name,
            'location': self,location,
            'time': self.time
        }







    
        










