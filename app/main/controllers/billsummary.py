from app.main.models import Bill, MONTHS
from app import db
from collections import OrderedDict

class BillSummary:
    def __init__(self, year = None):
        if year == None:
            self.year = str(datetime.datetime.now().year)
        else:
            self.year = str(year)

        
        


    def get_summary(self):
        self.summary = OrderedDict()
        for month in MONTHS:
            self.summary[month] = {'total': 0, 'approved': 0, 'paid': 0, 'incomplete': 0}
        self.summary['annual'] = {'total': 0, 'approved': 0, 'paid': 0, 'incomplete': 0}

        bills = Bill.query.filter_by(Year = self.year).all()
        for bill in bills:
            self.summary[bill.Month]['total'] += 1
            self.summary['annual']['total'] += 1

            if bill.IsCompleted:
                if bill.IsApproved:
                    self.summary[bill.Month]['approved'] += 1
                    self.summary['annual']['approved'] += 1

                if bill.IsPaid:
                    self.summary[bill.Month]['paid'] += 1
                    self.summary['annual']['paid'] += 1
            else:
                self.summary[bill.Month]['incomplete'] += 1
                self.summary['annual']['incomplete'] += 1

    def get_summary_barchart_data(self):
        self.get_summary()
        total = {'data': [], 'label': "Total"}
        approved = {'data': [], 'label': 'Approved'}
        paid = {'data': [], 'label': 'Paid'}
        incomplete = {'data': [], 'label': 'Not Completed'}

        for month in MONTHS:
            total['data'].append(self.summary[month]['total'])
            approved['data'].append(self.summary[month]['approved'])
            paid['data'].append(self.summary[month]['paid'])
            incomplete['data'].append(self.summary[month]['incomplete'])

        return [incomplete, paid, approved, total]


    def get_payment_amounts(self):
        bills = Bill.query.filter_by(Year = self.year).all()
        paid = {}
        total = {}

        for month in MONTHS:
            total[month] = 0
            paid[month] = 0

        for bill in bills:
            total[bill.Month] += bill.Total
            if bill.IsPaid:
                paid[bill.Month] =+ bill.Total

        remain = {}

        for month in MONTHS:
            remain[month] = str(total[month] - paid[month])
            total[month] = str(total[month])
            paid[month] = str(paid[month])

        return {'total': total, 'paid': paid, 'remain': remain}











