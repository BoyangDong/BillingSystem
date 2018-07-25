from app.main.models import GSECCode, Trader, MonthlyExpenses
from ... import db

class UpdateMonthlyEstimate(object):
	def __init__(self, args):
		self.year = args[0]
		self.month = args[1]
		self.code = args[2]
		self.amount = args[3]
		self.exp = self.create_or_update_monthly_estimate()
		
	# MonthlyExpenses(TraderOid, Month, Year, AverageExpense, RealExpense):
	def create_or_update_monthly_estimate(self):
		code_obj = GSECCode.query.filter_by(Code=self.code).first_or_404()
		trader = code_obj.Trader
		exp = MonthlyExpenses.query.filter_by(TraderOid=trader.Oid, Month=self.month, Year=self.year).first()
		if exp is None:
			total = sum([c.Amount for c in code_obj.Charges.all() if c.Bill.Month == self.month and c.Bill.Year == self.year])
			exp = MonthlyExpenses(trader.Oid, self.month, self.year, self.amount, total)
		else:
			exp.AverageExpense = self.amount
		exp.update_balance()
		db.session.add(exp)
		db.session.commit()
		return exp

	def get_result(self):
		return self.exp
