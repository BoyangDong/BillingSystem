from flask import url_for
from decimal import Decimal
from datetime import datetime
import uuid
from ... import db
from app.exceptions import ValidationError
from .vendor import Vendor
from .cashcard import CashCard
from .comp import YearMonth


def get_missing_filed_error_msg(missing_fields):
    if len(missing_fields) == 1:
        return (missing_fields[0] + ' is missing')
    if len(missing_fields) == 2:
        return (missing_fields[0]+' and ' + missing_fields[1] + ' are missing')
    if len(missing_fields) > 2:
        missing_fields[-1] = ', and ' + missing_fields[-1]
        return (', '.join(missing_fields) + ' are missing')


class Bill(db.Model, YearMonth):
    __tablename__ = 'bill'
    Oid = db.Column(db.String(38), primary_key = True, index=True)
    VendorShortcut = db.Column(db.String(38), db.ForeignKey('vendor.Shortcut'))
    Vendor = db.relationship("Vendor", backref=db.backref('bills', lazy='dynamic'))
    #Breakdowns backref defined in Breakdonw class
    Month = db.Column(db.String(4), index=True)
    Year = db.Column(db.String(4), index=True)
    Type = db.Column(db.String(32))
    Total = db.Column(db.Numeric(20, 2,asdecimal=False))
    IsCompleted = db.Column(db.Boolean)
    IsRebilled = db.Column(db.Boolean)
    IsPaid = db.Column(db.Boolean)
    IsApproved = db.Column(db.Boolean)

    BillNumber = db.Column(db.String(32))
    BillPayRef = db.Column(db.String(32))
    
    Created = db.Column(db.DateTime)
    CreatedBy = db.Column(db.String(38))


    def __init__(self, VendorShortcut, Month, Year, Total,Type=None):
        self.Oid = str(uuid.uuid4())
        self.VendorShortcut = VendorShortcut
        self.Month = Month
        self.Year = Year
        self.Total = Total
        self.IsCompleted = True
        self.IsRebilled = False
        self.IsPaid = False
        self.IsApproved = False
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        self.BillPayRef = ""
        self.Type = Type
        try:
            self.CreatedBy = g.current_user.username
        except:
            self.CreatedBy = None

    def check_breakdown_completion(self):
        total = Decimal('0.0')
        for bkd in self.Breakdowns.all():
            total += Decimal(bkd.Amount)
        if Decimal(total) >= self.Total:
            self.IsCompleted = True
            return True
        else:
            self.IsCompleted = False
            return False
        
    def update(self, json_bill):
        self.BillPayRef = json_bill.get('BillPayRef')
        self.BillNumber = json_bill.get('BillNumber')
        self.IsApproved = False
        VendorShortcut = json_bill.get('VendorShortcut')
        if VendorShortcut is not None:
            vendor = Vendor.query.filter_by(Shortcut=VendorShortcut).first()
            if vendor is None:
                raise ValidationError("New Vendor Does't exist")
            else:
                self.VendorShortcut = VendorShortcut
                self.Vendor = vendor
        Month = json_bill.get('Month')
        if Month is not None:
            self.Month = Month
        Year = json_bill.get('Year')
        if Year is not None:
            self.Year = Year
        Total = json_bill.get('Total')
        if Total is not None:
            self.Total = Decimal(Total)
        Type = json_bill.get('Type')
        if Type is not None:
            self.Type = Type
        IsPayed = json_bill.get('IsPayed')
        if IsPayed is not None:
            self.IsPayed = IsPayed

        services = vendor.Services

        for bkd in self.Breakdowns.all():
            if not bkd.Detail in services:
                bkd.Detail = ""
        Breakdowns = json_bill.get('Breakdowns')
        total = Decimal('0.0')
        if Breakdowns is not None and type(Breakdowns) is list:
            for bkd in Breakdowns:
                total += Decimal(bkd.get('Amount'))
                if not bkd.get('Oid'):
                    bkd['BillOid'] = self.Oid
                    new_bkd = Breakdown.from_json(bkd)
                    self.Breakdowns.append(new_bkd)
                    db.session.add(new_bkd)
                else:
                    temp_bkd = self.Breakdowns.filter_by(Oid=bkd.get('Oid')).first()
                    if temp_bkd is not None:
                        temp_bkd.update(bkd)



    def to_json(self):

        json_bill = {
        'Oid' : self.Oid,
        'VendorShortcut' : self.VendorShortcut,
        'Type' : self.Type,
        'Breakdowns' : [breakdown.to_json() for breakdown in self.Breakdowns.all()],
        'Month' : self.Month,
        'Year' : self.Year,
        'Total' : str(self.Total),
        'IsCompleted' : self.IsCompleted,
        'IsApproved' : self.IsApproved,
        'IsPaid' : self.IsPaid,
        'BillPayRef' : self.BillPayRef,
        'BillNumber' : self.BillNumber,
        'Created' : self.Created,
        'CreatedBy' : self.CreatedBy
        }
        return json_bill

    @staticmethod
    def from_json(json_bill):
        missing_fields = []


        VendorShortcut = json_bill.get('VendorShortcut')
        if VendorShortcut is None: missing_fields.append('VendorShortcut')
        month = json_bill.get('Month')
        if month is None: missing_fields.append('Month')
        year = json_bill.get('Year')
        if year is None: missing_fields.append('Year')
        total = json_bill.get('Total')
        if total is None : missing_fields.append('Total')
        Type = json_bill.get('Type')

   

        if len(missing_fields) == 0:
            b = Bill(VendorShortcut, month, year, total, Type)
            b.BillNumber = json_bill.get('BillNumber')
            return b
        else:
            raise ValidationError(get_missing_filed_error_msg(missing_fields))

    def to_cash_card(self):
        res = []
        for breakdown in self.Breakdowns.all():
            res.append(breakdown.to_cash_card('C'))
            res.append(breakdown.to_cash_card('D'))
        return res

from .breakdown import Breakdown


















        






