import uuid
from datetime import datetime
from ... import db
from app.exceptions import ValidationError

association_table = db.Table('people_addresses_association',
    db.Column('Person_Oid', db.String(38), db.ForeignKey('person.Oid')),
    db.Column('Address_Oid', db.String(38), db.ForeignKey('address.Oid')),
    db.UniqueConstraint('Person_Oid', 'Address_Oid')
    )


class Address(db.Model):
    __tablename__ = 'address'
    Oid = db.Column(db.String(38), primary_key=True, index=True)
    Street = db.Column(db.String(64))
    Unit = db.Column(db.String(64)) #apt. unit. etc.
    City = db.Column(db.String(32))
    State = db.Column(db.String(32))
    ZipCode = db.Column(db.String(16))
    Country = db.Column(db.String(32))
    People = db.relationship('Person', secondary=association_table,
        backref=db.backref('Addresses', lazy='dynamic'), lazy='dynamic')
    AddressType = db.Column(db.String(16))
    Created = db.Column(db.DateTime)
    CreatedBy = db.Column(db.String(38))

    def __init__(self, Street, City, State, ZipCode, AddressType, Country, Unit=None):
        self.Oid = str(uuid.uuid4())
        self.Street = Street
        self.Unit = Unit
        self.City = City
        self.State = State
        self.ZipCode = ZipCode
        self.Country = Country
        #self.PersonOid = PersonOid   <-- removed
        self.AddressType = AddressType
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")

    def to_json(self):
        return {
        'Oid' : self.Oid,
        'Street' : self.Street,
        'Unit' : self.Unit,
        'City' : self.City,
        'State' : self.State,
        'ZipCode' : self.ZipCode,
        'Country' : self.Country,
        'AddressType' : self.AddressType,
        'Created' : self.Created
        }


    def update(self, json_addr):
        self.Street = json_addr.get('Street')
        self.Unit = json_addr.get('Unit')
        self.City = json_addr.get('City')
        self.State = json_addr.get('State')
        self.ZipCode = json_addr.get('ZipCode')
        self.Country = json_addr.get('Country')
        self.AddressType = json_addr.get('AddressType')



    @staticmethod
    def from_json(json_addr):
        Street = json_addr.get('Street')
        Unit = json_addr.get('Unit')
        City = json_addr.get('City')
        State = json_addr.get('State')
        ZipCode = json_addr.get('ZipCode')
        Country = json_addr.get('Country')
        AddressType = json_addr.get('AddressType')

        return Address(Street, City, State, ZipCode, AddressType, Country, Unit)




