from flask_login import UserMixin
from app.mep_dashboard import db


class Departments(db.Model):

    __tablename__ = 'Departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), index=True, unique=True)
    acronym = db.Column(db.String(8), index=True, unique=True)
    head_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    is_active = db.Column(db.Integer)

    def __init__(self, name, acronym, head_id=None, is_active=0):
        self.name = name
        self.acronym = acronym
        self.head_id = head_id
        self.is_active = is_active

    def __repr__(self):
        return self.name


class Teams(db.Model):

    __tablename__ = 'Teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), index=True, unique=True)
    dpt_id = db.Column(db.Integer, db.ForeignKey('Departments.id'))
    lead_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    head_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    section_name = db.Column(db.String(8))
    is_active = db.Column(db.Integer)

    def __init__(self, name, dpt_id=None, lead_id=None, head_id=None, section_name=None, is_active=0):
        self.name = name
        self.dpt_id = dpt_id
        self.lead_id = lead_id
        self.head_id = head_id
        self.section_name = section_name
        self.is_active = is_active

    def __repr__(self):
        return self.name


class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8), index=True, unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('Teams.id'))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_in = db.Column(db.DateTime)
    last_connection = db.Column(db.DateTime)
    is_active = db.Column(db.Integer)

    def __init__(self, username, team_id, first_name=None, last_name=None, date_in=None, last_connection=None,
                 is_active=1):
        self.username = username
        self.team_id = team_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_in = date_in
        self.last_connection = last_connection
        self.is_active = is_active

    def __repr__(self):
        return self.name

#    @staticmethod
#    def try_login(username, password):
#        s = Server(host=ldap_host, port=int(ldap_port), get_info=ALL)
#        c = Connection(s, user=username + ldap_suffix, password=password)
#        c.bind()