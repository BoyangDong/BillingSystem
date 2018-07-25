import uuid
from ... import db
from datetime import datetime
from app.exceptions import ValidationError
from flask import url_for




class GSECCode(db.Model):
    __tablename__ = 'gseccode'
    #Oid = db.Column(db.String(38), primary_key=True)
    Code = db.Column(db.String(8), primary_key=True, index=True)
    AccountType = db.Column(db.String(38))
    TraderOid = db.Column(db.String(38), db.ForeignKey('trader.Oid'))

    CreatedBy = db.Column(db.String(38))
    StartDate = db.Column(db.DateTime)
    EndDate = db.Column(db.DateTime)

    #Charges = db.relationship('Breakdown', backref=gseccode, lazy='dynamic')

    #Credits
    #trader has Charges, and firm has Credits

    SortingScore = db.Column(db.Integer)

    Created = db.Column(db.DateTime)

    def __init__(self, Code, AccountType="Trader Account", StartDate=None, EndDate=None):
        self.Code = Code
        self.AccountType = AccountType
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        self.SortingScore = 0


    def get_monthly_charges(self, year=None, month=None):
        if year == None or month == None:
            year = datetime.now().strftime("%y")
            month = datetime.now().strftime("%b").upper()

        charges = []
        for charge in self.Charges.all():
            #trailer = charge.Trailer.split('_')
            #
            #
            if (year, month) == charge.get_year_month():
                charges.append(charge.Amount)
        return charges





    def to_json(self):
        return {
        "Code" : self.Code,
        "AccountType" : self.AccountType,
        "TraderOid" : self.TraderOid,
        "ChargeOids" : [breakdown.Oid for breakdown in self.Charges.all()],
        "CreditOids" : [breakdown.Oid for breakdown in self.Credits.all()],
        "StartDate": self.StartDate,
        "EndDate": self.EndDate,
        "Created" : self.Created
        }

    def update(self, json_gsec):
        pass

    @staticmethod
    def from_json(json_gsec):
        Code = json_gsec.get('Code')

        if Code is None or Code is "":
            raise ValidationError('GSEC Code Not Given')

        AccountType = json_gsec.get('AccountType')
        if AccountType is None or AccountType is "":
            raise ValidationError('GSEC AccountType is required')

        StartDate = json_gsec.get('StartDate')
        if StartDate is not None:
            StartDate = datetime.datetime.strptime(StartDate,"%Y-%m-%d")
        EndDate = json_gsec.get('EndDate')
        if EndDate is not None:
            EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
        return GSECCode(Code, AccountType, StartDate, EndDate)







