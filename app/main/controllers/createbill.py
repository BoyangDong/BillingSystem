from app.main.models import Bill, Breakdown
from ... import db

class CreateBill(object):
	def create(self, json):
		json_breakdown = json.get("Breakdowns")
		

