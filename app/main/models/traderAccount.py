import uuid
from datetime import datetime
from ... import db
from app.exceptions import ValidationError
from flask import url_for


class TraderAccount(db.Model):
    '''traders' vendor accounts
    '''
    __tablename__ = 'traderaccount'
    Oid = db.Column(db.String(38), primary_key = True)
    TraderOid = db.Column(db.String(38), db.ForeignKey('trader.Oid'))
    #trader backref defined in Trader class
    AccountType = db.Column(db.String(16), db.ForeignKey('vendor.Shortcut'))
    Vendor = db.relationship("Vendor", backref=db.backref('traderaccounts', lazy='dynamic'))
    AccountNumber = db.Column(db.String(16))
    Created = db.Column(db.DateTime)
    CreatedBy = db.Column(db.String(38))


    def __init__(self, TraderOid, AccountType, AccountNumber):
        self.Oid = str(uuid.uuid4())
        self.TraderOid = TraderOid
        self.AccountType = AccountType
        self.AccountNumber = AccountNumber
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")

    def to_json(self):
        json_tdracc = {
        'Oid' : self.Oid,
        'TraderOid' : self.TraderOid,
        'AccountType' : self.AccountType,
        'AccountNumber' : self.AccountNumbern,
        'Created' : self.Created
        }
        return json_tdracc;

    @staticmethod
    def from_json(json_tdracc):
        TraderOid = json_tdracc.get('TraderOid')
        if TraderOid is None or TraderOid is "":
            raise ValidationError("Trader Not Found")
        AccountType = json_tdracc.get('AccountType')
        if AccountType is None or AccountType is "":
            raise ValidationError("Account Type Undefined")
        AccountNumber = json_tdracc.get('AccountNumber')
        if AccountNumber is None or AccountNumber is "":
            raise ValidationError("Account Number Missing")
        return TraderAccount(TraderOid, AccountType, AccountNumber)

