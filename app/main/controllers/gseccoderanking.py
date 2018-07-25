from app.main.models import Bill

class Score:
	def __init__(self):
		self.pairs = {}
		self._get_number_of_records_from_db()

	def __getitem__(self, key):
		return self.pairs.get(key)

	def inc(self, key):
		n = self.pairs.get(key)
		if n is None:
			n = 0
		self.pairs[key] = n + 1

	def _get_number_of_records_from_db(self):
		for bill in Bill.query.all():
			for bkd in bill.Breakdowns.all():
				self.inc(bkd.GSECCode)
