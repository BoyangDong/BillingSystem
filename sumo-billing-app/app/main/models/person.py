import uuid
from ... import db
from datetime import datetime
from app.exceptions import ValidationError
from .address import Address
from .phone import Phone
from .email import Email


class Person(db.Model):
    __tablename__ = 'person'
    Oid = db.Column(db.String(38), primary_key=True, index=True)
    FirstName = db.Column(db.String(36))
    LastName = db.Column(db.String(36))
    Title = db.Column(db.String(36))
    Phones = db.relationship('Phone', backref='person', lazy='dynamic')
    Emails = db.relationship('Email', backref='person', lazy='dynamic')
    #Addresses = db.relationship('Address', backref='person', lazy='dynamic') <-- moved to address as relationship
    Created = db.Column(db.DateTime)
    TraderOid = db.Column(db.String(36), db.ForeignKey('trader.Oid'))
    CreatedBy = db.Column(db.String(38))

    def __init__(self, FirstName, LastName, Title, TraderOid=None):
        self.Oid = str(uuid.uuid4())
        self.FirstName = FirstName
        self.LastName = LastName
        self.Title = Title
        self.TraderOid = TraderOid
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")


    def to_json(self):
        return {
        'Oid' : self.Oid,
        'FirstName' : self.FirstName,
        'LastName' : self.LastName,
        'Title' : self.Title,
        'Phones' : [phone.to_json() for phone in self.Phones.all()],
        'Emails' : [email.to_json() for email in self.Emails.all()],
        'Addresses' : [address.to_json() for address in self.Addresses.all()],
        'Created' : self.Created
        }


    def update(self, json_person):
        self.FirstName = json_person.get('FirstName')
        self.LastName = json_person.get('LastName')
        self.Title = json_person.get('Title')

        for address in json_person.get('Addresses'):
            addr = Address.query.filter_by(Oid=address.get('Oid')).first()
            if addr is not None:
                addr.update(address)
            else:
                addr = Address.from_json(address)
                self.Addresses.append(addr)
                db.session.add(addr)

        for phone in json_person.get('Phones'):
            ph = Phone.query.filter_by(Oid=phone.get('Oid')).first()
            if ph is not None:
                ph.update(phone)
            else:
                ph = Phone.from_json(phone)
                self.Phones.append(ph)
                db.session.add(addr)

        for email in json_person.get('Emails'):
            em = Email.query.filter_by(Oid=email.get('Oid')).first()
            if em is not None:
                em.update(email)
            else:
                em = Email.from_json(email)
                self.Emails.append(em)
                db.session.add(em)
        




    @staticmethod
    def from_json(json_person):
        FirstName = json_person.get('FirstName')
        LastName = json_person.get('LastName')
        Title = json_person.get('Title')


        Addresses = json_person.get('Addresses') or []

        Addresses = [Address.from_json(addr) for addr in Addresses]
        for addr in Addresses:
            db.session.add(addr)

        TraderOid = json_person.get('TraderOid')

        person = Person(FirstName, LastName, Title, TraderOid)

        person.Addresses.extend(Addresses)

        Phones = json_person.get('Phones') or []
        for phone in Phones:
            phone['PersonOid'] = person.Oid

        Phones = [Phone.from_json(phone) for phone in Phones]
        for phone in Phones:
            db.session.add(phone)
        person.Phones.extend(Phones)


        emails = json_person.get('Emails') or []
        for email in emails:
            email['PersonOid'] = person.Oid
            em = Email.from_json(email)
            db.session.add(em)
            person.Emails.append(em)
            
        return person



