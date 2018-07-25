import uuid
from ... import db
from datetime import datetime
from app.exceptions import ValidationError


class Email(db.Model):
	__tablename__ = 'email'
	Oid = db.Column(db.String(38), primary_key=True, index=True)
	PersonOid = db.Column(db.String(38), db.ForeignKey('person.Oid'))
	Email = db.Column(db.String(64))
	Type = db.Column(db.String(16))
	Created = db.Column(db.DateTime)
	#person backref defined in Person class


	def __init__(self, PersonOid, Email, Type):
		self.Oid = str(uuid.uuid4())
		self.PersonOid = PersonOid
		self.Email = Email
		self.Type = Type
		self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")


	def to_json(self):
		return {
		'Oid' : self.Oid,
		'PersonOid' : self.PersonOid,
		'Email' : self.Email,
		'Type' : self.Type,
		'Created' : self.Created
		}

	def update(self, json_email):
		self.Email = json_email.get('Email')
		self.Type = json_email.get('Type')

	@staticmethod
	def from_json(json_email):
		PersonOid = json_email.get('PersonOid')
		email = json_email.get('Email')
		Type = json_email.get('Type')
		return Email(PersonOid, email, Type)
		
