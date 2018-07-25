import uuid
from ... import db
from datetime import datetime
from app.exceptions import ValidationError



class Phone(db.Model):
    __tablename__ = 'phone'
    Oid = db.Column(db.String(38), primary_key=True, index=True)
    Number = db.Column(db.String(16))
    Type = db.Column(db.String(16))
    #person backref defined in Person class
    PersonOid = db.Column(db.String(38), db.ForeignKey('person.Oid'))
    Created = db.Column(db.DateTime)

    def __init__(self, Number, Type, PersonOid):
        self.Oid = str(uuid.uuid4())
        self.Number = Number
        self.Type = Type
        self.PersonOid = PersonOid
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")


    def to_json(self):
        return {
        'Oid' : self.Oid,
        'Number' : self.Number,
        'Type' : self.Type,
        'PersonOid' : self.PersonOid,
        'Created' : self.Created
        }

    def update(self, json_phone):
        self.Number = json_phone.get('Number')
        self.Type = json_phone.get('Type')


    @staticmethod
    def from_json(json_phone):
        Number = json_phone.get('Number')
        Type = json_phone.get('Type')
        PersonOid =json_phone.get('PersonOid')
        return Phone(Number,Type,PersonOid)
        



