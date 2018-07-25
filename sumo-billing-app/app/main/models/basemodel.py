from abc import ABCMeta, abstractmethod

class BaseModel(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def from_json(self, json_str):
		pass

	@abstractmethod
	def to_json(self):
		pass

	@abstractmethod
	def update(self, json_str):
		pass


from . import *
BaseModel.register(Address)
BaseModel.register(Bill)
BaseModel.register(Breakdown)
BaseModel.register(Email)
BaseModel.register(GSECCode)
BaseModel.register(MonthlyExpenses)
BaseModel.register(Person)
BaseModel.register(Phone)
BaseModel.register(Trader)
BaseModel.register(Vendor)

assert issubclass(MonthlyExpenses, MyABC)
assert issubclass(Trader, MyABC)