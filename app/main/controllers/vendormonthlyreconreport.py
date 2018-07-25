from report import ReportBase
from io import BytesIO
from datetime import datetime
from app.main.models import MONTHS
import xlsxwriter


class VendorMonthlyReconReport(ReportBase):
    def get_report_xlsx(self, data):
        ''' data format
        data = [
            {
                "vendor" : "vendor name",
                "report" : [
                    {
                        "JAN" : "amount of money",
                        "FEB" : "amount of money",
                        ...
                        ...
                        ...
                        "DEC" : "amount of money",
                        "name": "name is either 'Total' or gsec account number
                    } ,
                    {
                        ...
                    }
                ]
            }
        ]
        '''

        output = BytesIO()
        options = {'strings_to_numbers': True,
             'default_date_format': 'mm/dd/yy',
             'remove_timezone': True, 'in_memory': True}
        workbook = xlsxwriter.Workbook(output, options)
        worksheet = workbook.add_worksheet("Vendors Report")
        year = str(datetime.now().year)
        title = "Vendor Report %d" %(datetime.now().year)
        title_format = workbook.add_format({'bold': True, 'align': 'center',
                                            'valign': 'vcenter', 'border': 1,
                                            'bg_color': '#42c2f4',
                                            'font_size': 22})
        worksheet.merge_range('E1:J2', title, title_format)
        bold = workbook.add_format({'bold': True, 'align': 'center'})
        col = 0
        worksheet.write(2, 0, "Vendor", bold)
        for month in MONTHS:
            col += 1
            worksheet.write(2, col, month, bold)
        row_begin = 3
        for vendor_report in data:
            self._write_vendor_report(row_begin, vendor_report, worksheet, workbook)
            row_begin += len(vendor_report.get('report'))
        worksheet.set_column(1, 14, 10)
        workbook.close()
        output.seek(0)
        return output


    def _write_vendor_report(self, row, vendor_report, worksheet, workbook):
        total_format = workbook.add_format({'bold': True, 'align': 'center', 'num_format': '$#,##0.00'})
        account_format = workbook.add_format({'align': 'center', 'num_format': '$#,##0.00'})
        col, i = 0, 1
        for account in vendor_report.get('report'):
            if account.get('name') == 'Total':
                worksheet.write(row, 0, vendor_report.get('vendor'), total_format)
                for month in MONTHS:
                    col += 1
                    worksheet.write(row, col, account.get(month), total_format)
                col = 0
            else:
                worksheet.write(row + i, col, account.get('name'), account_format)
                for month in MONTHS:
                    col += 1
                    worksheet.write(row + i, col, account.get(month), account_format)
                col = 0
                i += 1

