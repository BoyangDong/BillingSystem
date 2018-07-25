from report import ReportBase
from io import BytesIO
from datetime import datetime
from app.main.models import MONTHS
import xlsxwriter

class GSECMonthlyReconReport(ReportBase):


	def get_report_xlsx(self, data):
		''' data should have a format of {'gseccode':'3CT8', 'data': [{'JAN":"10", "FEB":"...", ...'},{...}]}
		'''

		output = BytesIO()
		options = {'strings_to_numbers':True, 'default_date_format': 'mm/dd/yy', 'remove_timezone': True, 'in_memory': True}

		width = {} # tracking the max width of each coloumn

		workbook = xlsxwriter.Workbook(output, options)

		worksheet = workbook.add_worksheet(data.get('gseccode'))
		title = data.get('gseccode')
		year = str(datetime.now().year)

		data = data.get('data')

		estimate = data[-1]
		difference = data [-2]
		body = sorted(data[:-2], key=lambda x: x['name'])

		money_format = workbook.add_format({'num_format': '$#,##0.00'})
		est_diff_format = workbook.add_format({'num_format': '$#,##0.00',
                                         'bold': True})
		est_diff_format.set_top(2)
		est_diff_format.set_bottom(2)
		bold = workbook.add_format({'bold': True, 'align': 'center'})



		title_format = workbook.add_format({'bold': True, 'align': 'center',
                                      'valign': 'vcenter', 'border': 1,
                                      'bg_color': '#ADD8E6', 'font_size': 22})

		worksheet.merge_range('G2:I3' ,title, title_format)


		col = 2
		worksheet.write(4, 1, year, bold)
		for month in MONTHS:
			worksheet.write(4, col, month, bold)
			col += 1

		col = 2
		worksheet.write(5,1, 'ESTIMATE', est_diff_format)
		for month in MONTHS:
			worksheet.write(5, col, estimate.get(month), est_diff_format)
			col += 1

		col = 1
		row = 7

		for line in body:
			worksheet.write(row, col, line.get('name'))
			col += 1
			for month in MONTHS:
				worksheet.write(row, col, line.get(month), money_format)
				col +=1

			row += 1
			col =1



		col = 2
		row = row + 1

		worksheet.write(row, 1, 'DIFFERENCE', est_diff_format)

		for month in MONTHS:
			worksheet.write(row, col, difference.get(month), est_diff_format)
			col += 1


		worksheet.set_column(1,14, 10)


		workbook.close()
		output.seek(0)
		return output

















