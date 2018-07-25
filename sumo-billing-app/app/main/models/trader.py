from datetime import datetime
import uuid
from ... import db
from app.exceptions import ValidationError
from .person import Person
from .gseccode import GSECCode
from flask import url_for
from decimal import Decimal

class Trader(db.Model):
    __tablename__ = 'trader'
    Oid = db.Column(db.String(38), primary_key=True, index=True)
    Contacts = db.relationship('Person', backref="Trader",lazy='dynamic')
    Group = db.Column(db.String(64))
    VendorAccounts = db.relationship('TraderAccount', backref='trader', lazy='dynamic')
    SubscribedServices = db.relationship('SubscribedService', backref='trader', lazy='dynamic')
    gseccodes = db.relationship('GSECCode', backref='Trader', lazy='dynamic')
    Created = db.Column(db.DateTime)
    BeginningMonthlyCharge = db.Column(db.Numeric(20, 2,asdecimal=False))
    #monthlyexpenses backref defined in MonthlyExpenses class
    #gseccodes backref defined in GSECCode class
    CreatedBy = db.Column(db.String(38))


    def __init__(self, Group=None, BeginningMonthlyCharge=0):
        self.Oid = str(uuid.uuid4())
        self.Group = Group
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        self.BeginningMonthlyCharge = BeginningMonthlyCharge


    def _update_balance(self, exp):
        exp.update_balance()
        db.session.commit()
        return exp.to_json()

    def update(self, json_tdr):
        self.Group = json_tdr.get('Group')
        charge = json_tdr.get('BeginningMonthlyCharge')
        if charge is None:
            self.BeginningMonthlyCharge = 0
        else:
            self.BeginningMonthlyCharge = Decimal(charge)

        for contact in json_tdr.get('Contacts'):
            c = Person.query.filter_by(Oid=contact.get('Oid')).first()
            if c is None:
                contact['TraderOid'] = self.Oid
                c = Person.from_json(contact)
                self.Contacts.append(c)
                db.session.add(c)
            else:
                c.update(contact)

        cur_gs_lst = [gs.Code for gs in self.gseccodes.all()]

        for gseccode in json_tdr.get('GSECCodes'):
            gs = GSECCode.query.filter_by(Code=gseccode.get('Code')).first()
            if gs is None:
                gs = GSECOCode.from_json(gseccode)
                self.gseccodes.append(gs)
                db.session.add(gs)
            elif gs.Code in cur_gs_lst:
                gs.update(gseccode)
           

    def to_json(self):
        json_tdr = {
        'Oid' : self.Oid,
        'Contacts' : [person.to_json() for person in self.Contacts.all()],
        'Group' : self.Group,
        'BeginningMonthlyCharge' : str(self.BeginningMonthlyCharge) ,
        'MonthlyExpenses' : [expense.to_json() for expense in self.monthlyexpenses.all()],
        'GSECCodes' : [code.to_json() for code in self.gseccodes.all()] ,
        'Created' : self.Created}
        return json_tdr

    @staticmethod
    def from_json(json_tdr):

        Group = json_tdr.get('Group')
        BeginningMonthlyCharge = json_tdr.get('BeginningMonthlyCharge') or 0
        trader = Trader(Group, BeginningMonthlyCharge)


        for contact in json_tdr.get('Contacts'):
            c = Person.from_json(contact)
            trader.Contacts.append(c)
            db.session.add(c)

        for gsec in json_tdr.get("GSECCodes"):
            g = GSECCode.from_json(gsec)
            trader.gseccodes.append(g)
            db.session.add(g)
  
        return trader


from .monthlyexpenses import MonthlyExpenses
