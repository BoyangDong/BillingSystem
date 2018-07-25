from abc import ABCMeta, abstractmethod

class ReportBase:
	__metaclass__ = ABCMeta

	@abstractmethod
	def get_report_xlsx(self, data):
		pass

		