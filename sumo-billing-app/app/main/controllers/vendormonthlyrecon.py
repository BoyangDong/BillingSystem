import datetime
from app.main.models import Vendor, MONTHS
from decimal import Decimal
import time

class VendorMonthlyRecon(object):
    def __init__(self, vendorShortcut = None, year = None):
        self.vendor = vendorShortcut
        if year == None:
            self.year = str(datetime.datetime.now().year)
        else:
            self.year = str(year)

        #self.report = self.getReport()

    def getReport(self, vendor=None, year=None):
        if vendor is None:
            vendor = Vendor.query.filter_by(Shortcut = self.vendor).first_or_404()
        bills = vendor.bills.filter_by(Year = year or self.year, IsCompleted=True).all() or []

        vendor_bill_record = {}

        table = {}
        for bill in bills:
            vendor_bill_record.setdefault(bill.Month, [])
            for bkd in bill.Breakdowns:
                vendor_bill_record[bill.Month].append(bkd.GSECCode)
                line = table.setdefault(bkd.GSECCode, {})
                monthly_amount = line.setdefault(bill.Month, Decimal(0))
                line[bill.Month] = monthly_amount + Decimal(bkd.Amount).quantize(Decimal("1.00"))
        res = []
        for k,v in table.items():
            line = {'name':k}
            for month in MONTHS:
                amount = v.get(month)
                if amount != None:
                    line[month] = str(amount)
                else:
                    line[month] = "0"
            res.append(line)

        total = {'name':"Total"}

        if len(res) == 0:
            for month in MONTHS:
                total[month] = Decimal("0.00")

        for line in res:
            for month in MONTHS:
                monthly_amount = total.setdefault(month, Decimal("0.00"))
                total[month] = Decimal(line.get(month) or Decimal("0.00")) + monthly_amount
                total[month] = total[month].quantize(Decimal("1.00"))
        for k, v in total.items():
            total[k] = str(v)

        for line in res:
            code = line.get('name')
            for month in MONTHS:
                amount = line.get(month)
                if Decimal(amount) == Decimal('0'):
                    codes = vendor_bill_record.get(month) or []
                    if codes == []:
                        line[month] = "$-.--"
                    elif code not in codes:
                        line[month] = "$-.--"
        month_records = set([b.Month for b in bills])
        for month in MONTHS:
            if month not in month_records:
                total[month] = "$-.--"
        res.append(total)
        return res

    def getAllReports(self, year=None):
        start = time.time()
        if year == None:
            self.year = str(datetime.datetime.now().year)

        reports = []
        for vendor in Vendor.query.all():
            report = {}
            report['industry'] = vendor.Industry
            report['vendor'] = vendor.Shortcut
            report['report'] = self.getReport(vendor, year)
            reports.append(report)

        end = time.time()
        print "GET Vendors Report Execution Time: ", (end - start)
        return reports






