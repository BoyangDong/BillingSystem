import uuid
from ... import db
from datetime import datetime
from app.exceptions import ValidationError
from flask import url_for
from .address import Address
from .email import Email
from .phone import Phone
from .person import Person

association_table = db.Table('vendor_contact_association',
    db.Column('Vendor_Shortcut', db.String(38), db.ForeignKey('vendor.Shortcut')),
    db.Column('Person_Oid', db.String(38), db.ForeignKey('person.Oid')),
    db.UniqueConstraint('Vendor_Shortcut', 'Person_Oid', name='UC_Vendor_Person_ids')
    )

class Vendor(db.Model):
    __tablename__ = 'vendor'
    Shortcut= db.Column(db.String(16), primary_key = True, index=True)
    Name = db.Column(db.Text)
    Contacts = db.relationship('Person', secondary=association_table,
        backref=db.backref('vendors', lazy='dynamic'), lazy='dynamic')
    AddressOid = db.Column(db.String(38), db.ForeignKey('address.Oid'))
    Address = db.relationship('Address')
    PaymentInstruction = db.Column(db.Text)
    ServiceSubscribers = db.relationship('SubscribedService', backref='vendor', lazy='dynamic')
    Created = db.Column(db.DateTime)
    TIN = db.Column(db.String(16))
    Services = db.Column(db.PickleType)
    Industry = db.Column(db.Text)
    #bills backref defined in Breakdown Bill class
    #traderaccounts backref defined in TraderAccount class
    CreatedBy = db.Column(db.String(38))

    def __init__(self, Shortcut, Name, Services, TIN=None, AddressOid=None, PaymentInstruction=None, Industry=None):
        self.Shortcut = Shortcut.upper()
        self.Name = Name
        self.PaymentInstruction = PaymentInstruction
        self.AddressOid = AddressOid
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        self.TIN = TIN
        self.Services = Services

    def to_json(self):
        if self.Address is None:
            address = Address.query.filter_by(Oid=self.AddressOid).first()
            address = address.to_json()
        else:
            address = self.Address.to_json()
        return {
        "Shortcut" : self.Shortcut,
        "Name" : self.Name,
        "TIN" : self.TIN,
        "Contacts" : [contact.to_json() for contact in self.Contacts.all()],
        "Address" : address,
        "Services": self.Services,
        "Industry": self.Industry,
        "PaymentInstruction" : self.PaymentInstruction,
        "ServiceSubscribers" : [ sub.Oid for sub in self.ServiceSubscribers.all()],
        "Created" : self.Created,
        "Bills" : [ bill.to_json() for bill in self.bills.all()],
        "TraderAccounts" : [acct.Oid for acct in self.traderaccounts.all()]
        }

    def update(self, json_vendor):
        name = json_vendor.get('Name')
        if name is not None:
            self.Name = name
        pi = json_vendor.get('PaymentInstruction')
        if pi is not None:
            self.PaymentInstruction = pi
        tin = json_vendor.get('TIN')
        if tin is not None:
            self.TIN = tin
        services = json_vendor.get('Services')
        if services is not None:
            self.Services = services
        industry = json_vendor.get('Industry')
        if industry is not None:
            self.Industry = industry

        address = json_vendor.get('Address')
        if address is not None:
            if self.Address is None:
                new_address = Address.from_json(address)
                db.session.add(new_address)
                self.AddressOid = new_address.Oid
                self.Address = new_address
            else:
                self.Address.update(address)

        for contact in json_vendor.get('Contacts'):
            c = Person.query.filter_by(Oid=contact.get('Oid')).first()
            if c is not None:
                c.update(contact)
            else:
                c = Person.from_json(contact)
                self.Contacts.append(c)
                db.session.add(c)

            self.Contacts.append(c)


    @staticmethod
    def from_json(json_vendor):
        Shortcut = json_vendor.get('Shortcut')
        if Shortcut is None or Shortcut is "":
            raise ValidationError("Vendor Shortcut Not Found")
        Name = json_vendor.get('Name')
        if Name is None or Name is "":
            raise ValidationError("Vendor name is required")
        TIN = json_vendor.get('TIN')
        Services = json_vendor.get('Services')

        Industry = json_vendor.get('Industry')

        address = json_vendor.get('Address')
        if address is not None:
            addr = Address.from_json(address)
            AddressOid = addr.Oid
            db.session.add(addr)
        else:
            AddressOid = None

        PaymentInstruction = json_vendor.get('PaymentInstruction')



        vendor = Vendor(Shortcut, Name, Services, TIN, AddressOid, PaymentInstruction, Industry)

        contacts = json_vendor.get("Contacts")
        for contact in contacts:
            conn = Person.from_json(contact)
            vendor.Contacts.append(conn)
            db.session.add(conn)

        return vendor




