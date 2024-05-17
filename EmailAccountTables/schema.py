from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SIP_Trunk(Base):
    __tablename__ = 'SIP_Trunks'

    sip_trunk_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    provider = Column(String(50))
    hostname = Column(String(100))
    port = Column(Integer)
    username = Column(String(50))
    password = Column(String(255))
    transport = Column(String(10), default='UDP')
    registration_required = Column(Boolean, default=True)
    registration_expiry = Column(Integer)
    codec_list = Column(Text)
    dtmf_mode = Column(String(20))
    outbound_proxy = Column(String(100))
    caller_id_format = Column(String(50))
    dialplan_context = Column(String(50))
    nat_enabled = Column(Boolean, default=False)
    nat_external_ip = Column(String(20))

class Email_Account(Base):
    __tablename__ = 'Email_Accounts'

    email_account_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    email_address = Column(String(100))
    provider = Column(String(50))
    auth_type = Column(String(20), default='password')
    protocol = Column(String(10))
    incoming_host = Column(String(100))
    incoming_port = Column(Integer)
    outgoing_host = Column(String(100))
    outgoing_port = Column(Integer)
    username = Column(String(50))
    password = Column(String(255))
    oauth_client_id = Column(String(100))
    oauth_client_secret = Column(String(255))
    oauth_refresh_token = Column(String(255))
    polling_interval = Column(Integer, default=60)
    attachments_location = Column(String(255))

class Email_Template(Base):
    __tablename__ = 'Email_Templates'

    template_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    subject = Column(String(255))
    body = Column(Text)

class Queue_Email_Template(Base):
    __tablename__ = 'Queue_Email_Templates'

    queue_id = Column(Integer, ForeignKey('Queues.queue_id'), primary_key=True)
    template_id = Column(Integer, ForeignKey('Email_Templates.template_id'), primary_key=True)

class Business_Hours(Base):
    __tablename__ = 'Business_Hours'

    business_hours_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

class Business_Hours_Schedule(Base):
    __tablename__ = 'Business_Hours_Schedule'

    business_hours_id = Column(Integer, ForeignKey('Business_Hours.business_hours_id'), primary_key=True)
    day_of_week = Column(String(10), primary_key=True)
    start_time = Column(Time)
    end_time = Column(Time)
    time_zone = Column(String(50))
    is_24_hours = Column(Boolean, default=False)

class Queue_Business_Hours(Base):
    __tablename__ = 'Queue_Business_Hours'

    queue_id = Column(Integer, ForeignKey('Queues.queue_id'), primary_key=True)
    business_hours_id = Column(Integer, ForeignKey('Business_Hours.business_hours_id'), primary_key=True)

class Chat_Queue_Waiting_Message(Base):
    __tablename__ = 'Chat_Queue_Waiting_Messages'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    queue_id = Column(Integer, ForeignKey('Queues.queue_id'))
    time_interval = Column(Integer)
    message_text = Column(Text)

class Chat_Hold_Message(Base):
    __tablename__ = 'Chat_Hold_Messages'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    queue_id = Column(Integer, ForeignKey('Queues.queue_id'))
    time_interval = Column(Integer)
    message_text = Column(Text)

class Chat_Phrase(Base):
    __tablename__ = 'Chat_Phrases'

    phrase_id = Column(Integer, primary_key=True, autoincrement=True)
    shortcut = Column(String(50))
    phrase_text = Column(Text)
    queue_id = Column(Integer, ForeignKey('Queues.queue_id'))
