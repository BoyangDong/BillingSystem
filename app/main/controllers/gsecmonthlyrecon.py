import datetime
from app.main.models import GSECCode, MONTHS
from decimal import Decimal 

class GSECMonthlyRecon(object):
    def __init__(self, gseccode, year=None):
        self.code = gseccode
        if year == None:
            self.year = str(datetime.datetime.now().year)
        else:
            self.year = str(year)

        self.report = self.getreport()

    def __bill_pred(self, bill):
        if bill.Type == "Bill" and bill.Total >= 0:
            return True
        elif bill.Type == "Credit" and bill.Total < 0:
            return True
        else:
            return False
    def __credit_pred(self, bill):
        return not self.__bill_pred(bill)


    def getreport(self):
        gseccode = GSECCode.query.filter_by(Code = self.code).first_or_404()
        trader = gseccode.Trader
        expenses = trader.monthlyexpenses.filter_by(Year = self.year).all()
        breakdowns = [gsec for gsec in gseccode.Charges.all() if gsec.Bill.Year == self.year and self.__bill_pred(gsec.Bill)]
        #vendornames = list(set([b.Bill.VendorShortcut for b in breakdowns]))
        credits = [gsec for gsec in gseccode.Charges.all() if gsec.Bill.Year == self.year and self.__credit_pred(gsec.Bill)]
        
        
        estimate = {"name":"ESTIMATE"}
        for month in MONTHS:
            for exp in expenses:
                if exp.Month == month:
                    estimate[month] = exp.AverageExpense
                    break 
            else:
                estimate[month] = Decimal(0)

        res = self.__calc_vendor_montly_amount(breakdowns)

        creds = self.__calc_vendor_montly_amount(credits)

        vendornames = res['JAN'].keys()
        creditornames = creds['JAN'].keys()


        difference = {"name": "DIFFERENCE"}
        for month in MONTHS:
            difference[month] = str(Decimal(estimate[month]) - sum(res[month].values()) + sum(creds[month].values()))

        table = []
        for vendor in vendornames:
            line = {"name": vendor}
            for month in MONTHS:
                line[month] = str(res[month][vendor] * Decimal(-1.0))
            table.append(line)

        for vendor in creditornames:
            line = {"name": vendor}
            for month in MONTHS:
                line[month] = str(creds[month][vendor])
            table.append(line)
        '''
        for line in table:
            for month in MONTHS:
                if Decimal(line[month]) == Decimal('0') and month not in [c.Bill.Month for c in credits] and month not in [c.Bill.Month for c in breakdowns]:
                    line[month] = None
        '''




        table.append(difference)
        for k,v in estimate.items():
            estimate[k] = str(v)
        table.append(estimate)

        return table


    def __calc_vendor_montly_amount(self, breakdowns):
        ''' this method converts breakdowns to a matrix of vendors by months 
            and renturns a dictionary of months as keys and the values are 
            also dictionaries of vendors as keys
        '''
        res = {}
        for month in MONTHS:
            col = {}
            for bkd in breakdowns:
                vendor = bkd.Bill.VendorShortcut
                amount = col.setdefault(vendor, Decimal(0))
                if bkd.Bill.Month == month:
                    col[vendor] = Decimal(bkd.Amount) + amount
                else:
                    col[vendor] = Decimal(0) + amount
            res[month] = col
        return res













        