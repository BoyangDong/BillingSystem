from datetime import datetime
import uuid
from ... import db
from app.exceptions import ValidationError
from .person import Person
from flask import url_for

class CashCard(db.Model):
	__tablename__ = "cashcard"
	Oid = db.Column(db.String(38), primary_key=True)
	Account = db.Column(db.String(16))
	DorC =db.Column(db.String(1))
	CCY = db.Column(db.String(4))
	Amount = db.Column(db.Numeric(20, 2,asdecimal=False))
	Code = db.Column(db.String(16))
	Description = db.Column(db.String(38))
	

	def __init__(self, Account, DorC, CCY, Amount, Code, Description):
		self.Oid = str(uuid.uuid4())
		self.Amount = Amount
		self.DorC = DorC
		self.CCY = CCY
		self.Account = Account
		self.Description = Description
		self.Code = Code

	@staticmethod
	def from_json(json_cashcard):
		try:
			Account = json_cashcard.get("Account")
			DorC = json_cashcard.get("DorC")
			Amount = json_cashcard.get("Amount")
			Description = json_cashcard.get("Trailer")
			Code = json_cashcard.get("Code")
			CCY = json_cashcard.get("CCY") or "USD"
			return CashCard(Account, DorC, CCY, Amount, Code, Description)
		except:
			raise  ValidationError('Failed creating CashCard Item')

	def to_json(self):
		return {
		"Oid": self.Oid,
		"Amount": self.Amount,
		"DorC": self.DorC,
		"CCY": self.CCY,
		"Account": str(self.Account),
		"Description": self.Description,
		"Code": self.Code
		}
	def to_list(self):
		return [self.Account, self.DorC, self.CCY, self.Amount, self.Code, self.Description]

	@staticmethod
	def getCashCardItems():
		return [item.to_list() for item in CashCard.query.all()]




