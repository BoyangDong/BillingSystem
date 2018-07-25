from datetime import datetime
from decimal import Decimal
import uuid
from ... import db
from flask import url_for
from app.exceptions import ValidationError
from .gseccode import GSECCode as GSECCode_cls
from .cashcard import CashCard

class Breakdown(db.Model):
    __tablename__ = 'breakdown'
    Oid = db.Column(db.String(38), primary_key = True, index=True)
    BillOid = db.Column(db.String(38), db.ForeignKey('bill.Oid'))
    Bill = db.relationship('Bill', backref=db.backref('Breakdowns', lazy='dynamic'))
    GSECCode = db.Column(db.String(38), db.ForeignKey('gseccode.Code'), index=True)
    #gseccode = db.relationship("GSECCode", backref=db.backref('Breakdowns', lazy='dynamic'))

    tradergseccode = db.relationship('GSECCode', backref=db.backref("Charges", lazy='dynamic') ,foreign_keys=[GSECCode])

    CounterAccount = db.Column(db.String(38), db.ForeignKey('gseccode.Code'))
    firmgseccode = db.relationship('GSECCode', backref=db.backref("Credits", lazy='dynamic'), foreign_keys=[CounterAccount])
    # NOTE # A Breakdown is a charge going from trader account to firm account, in somecases it goes the other way around
    #      # gseccode is trader account, and firmgseccode is firm account
    Detail = db.Column(db.String(64))
    Trailer = db.Column(db.String(38))
    Notes = db.Column(db.Text)
    Amount = db.Column(db.Numeric(20, 2,asdecimal=False))
    Created = db.Column(db.DateTime)
    CreatedBy = db.Column(db.String(38))


    def __init__(self, BillOid, GSECCode, CounterAccount, Detail, Trailer, Notes, Amount):
        self.Oid = str(uuid.uuid4())
        self.BillOid = BillOid
        self.GSECCode = GSECCode
        self.CounterAccount = CounterAccount
        self.Detail = Detail
        self.Amount = Amount
        self.Notes = Notes
        self.Trailer = Trailer
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        try:
            self.CreatedBy = g.current_user.username
        except:
            self.CreatedBy = None


        code = GSECCode_cls.query.filter_by(Code=GSECCode).first()
        if code is not None:
            code.SortingScore += 1

    
    def get_year_month(self):
        try:
            return self.Bill.Year , self.Bill.Month
        except:
            return None, None


    def update(self,json_breakdown):
        GSECCode = json_breakdown.get('GSECCode')
        if GSECCode is not None:
            self.GSECCode = GSECCode
        CounterAccount = json_breakdown.get('CounterAccount')
        if CounterAccount is not None:
            self.CounterAccount = CounterAccount
        Detail = json_breakdown.get('Detail')
        if Detail is not None:
            self.Detail = Detail
        Amount = json_breakdown.get('Amount')
        if Amount is not None:
            self.Amount = Decimal(Amount)
        Trailer = json_breakdown.get('Trailer')
        if Trailer is not None:
            self.Trailer = Trailer
        Notes = json_breakdown.get('Notes')
        if Notes is not None:
            self.Notes = Notes

    def to_json(self):
        json_breakdown = {
        'Oid' : self.Oid,
        'GSECCode': self.GSECCode,
        'CounterAccount' : self.CounterAccount,
        'Detail' : self.Detail,
        'Trailer' : self.Trailer,
        'Notes' : self.Notes,
        'Amount' : str(self.Amount),
        'Created' : self.Created,
        'CreatedBy' : self.CreatedBy
        }
        return json_breakdown

    @staticmethod
    def from_json(json_breakdown):
  
        BillOid = json_breakdown.get('BillOid')
        if BillOid is None or BillOid is "":
            raise ValidationError('Bill not found')
        gseccode = json_breakdown.get('GSECCode')
        CounterAccount = json_breakdown.get('CounterAccount')
        Detail = json_breakdown.get('Detail')
        Trailer = json_breakdown.get('Trailer')
        Amount = json_breakdown.get('Amount')
        Notes = json_breakdown.get('Notes')
        bkd = Breakdown(BillOid, gseccode, CounterAccount, Detail, Trailer, Notes, Amount)

        
        '''
        bill = Bill.query.filter_by(Oid=BillOid).first()
        gsec = GSECCode.query.filter_by(Code=gseccode).first_or_404()
        exp = gsec.Trader.create_monthlyexpenses(year=bill.Year, month=bill.Month);
        exp.update_realexpenses(bkd.Amount)
        '''
        return bkd 

    def update_monthlyexpenses(self):
        for exp in self.tradergseccode.Trader.monthlyexpenses.all():
            if exp.Month == self.Bill.Month and exp.Year == self.Bill.Year:
                #mexp = MonthlyExpenses.query.filter_by(Oid=exp.Oid).first()
                exp.RealExpense = Decimal(exp.RealExpense) - Decimal(self.Amount)
                exp.update_balance()
                break

    def on_delete(self):
        for exp in self.tradergseccode.Trader.monthlyexpenses.all():
            if exp.Month == self.Bill.Month and exp.Year ==self.Bill.Year:
                exp.RealExpense






    def to_cash_card(self, DorC):
        if DorC is "C":
            c = CashCard(Account=self.GSECCode+"5519", DorC="C", CCY="USD", Amount=self.Amount, Code="ACT", Description=self.Trailer)
            return c
        elif DorC is "D":
            c = CashCard(Account=self.CounterAccount+"5519", DorC="D", CCY="USD", Amount=self.Amount, Code="ACX", Description=self.Trailer)
            return c
        else:
            return None
          




from .monthlyexpenses import MonthlyExpenses    
from .bill import Bill
