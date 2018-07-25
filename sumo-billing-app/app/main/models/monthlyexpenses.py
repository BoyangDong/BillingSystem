import uuid
from ... import db
from datetime import datetime
from decimal import Decimal

from app.exceptions import ValidationError
from flask import url_for
from app.main.models import MONTHS


class MonthlyExpenses(db.Model):
    __tablename__ = 'monthlyexpenses'
    Oid = db.Column(db.String(38), primary_key=True, index=True)
    TraderOid = db.Column(db.String(38), db.ForeignKey('trader.Oid'))
    Trader = db.relationship('Trader', backref=db.backref('monthlyexpenses', lazy='dynamic'))
    Month = db.Column(db.String(8), index=True)
    Year = db.Column(db.String(4), index=True)
    AverageExpense = db.Column(db.Numeric(20, 2,asdecimal=False))
    RealExpense = db.Column(db.Numeric(20, 2,asdecimal=False))
    Balance = db.Column(db.Numeric(20, 2,asdecimal=False))
    Created = db.Column(db.DateTime)
    CreatedBy = db.Column(db.String(38))


    def __init__(self, TraderOid, Month, Year, AverageExpense, RealExpense):
        self.Oid = str(uuid.uuid4())
        self.TraderOid = TraderOid
        self.Month = Month
        self.Year = Year
        self.AverageExpense = Decimal(AverageExpense)
        self.RealExpense = Decimal(RealExpense)
        self.Balance = Decimal(RealExpense) - Decimal(AverageExpense)
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        try:
            self.CreatedBy = g.current_user
        except:
            self.CreatedBy = ""

    def __eq__(self, other):
        if self.Year == other.Year and self.Month == other.Month:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.Year < other.Year:
            return True
        if self.Year > other.Year:
            return False

        if MONTHS.index(self.Month) < MONTHS.index(other.Month):
            return True
        else:
            return False
    def __gt__(self, other):
        if self.Year < other.Year:
            return False
        if self.Year > other.Year:
            return True

        if MONTHS.index(self.Month) > MONTHS.index(other.Month):
            return True
        else:
            return False
            
    def __le__(self, other):
        if not self.__gt__(other):
            return True
        else:
            return False
    def __ge__(self, other):
        if not self.__lt__(other):
            return True
        else:
            return False



    def update_realexpenses(self, amount):
        self.RealExpense = Decimal(self.RealExpense) + Decimal(amount)
        self.update_balance()

    def update_balance(self):
        self.Balance =  Decimal(self.AverageExpense) - Decimal(self.RealExpense)

    def to_json(self):

        json_expense = {
        'Oid' : self.Oid,
        'TraderOid' : self.TraderOid,
        'Month' : self.Month,
        'Year' : self.Year,
        'AverageExpense' : str(self.AverageExpense),
        'RealExpense' : str(self.RealExpense),
        'Balance' : str(self.Balance),
        'Created' : self.Created
        }
        return json_expense


    @staticmethod
    def from_json(json_expense):
        TraderOid = json_expense.get('TraderOid')
        if TraderOid is None or Trader.query.filter_by(Oid=TraderOid).first() is None:
            raise ValidationError("Trader Not Identified")
        Month = json_expense.get('Month')
        if Month is None:
            raise ValidationError('Month Not Given')
        Year = json_expense.get('Year')
        if Year is None:
            raise ValidationError('Year Not Given')
        AverageExpense = json_expense.get('AverageExpense')
        RealExpense = json_expense.get('RealExpense')

        return MonthlyExpenses(TraderOid, Month, Year, AverageExpense, RealExpense)


from .trader import Trader