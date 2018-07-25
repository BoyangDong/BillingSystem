
import xlsxwriter
from io import BytesIO 
from datetime import datetime

def getCashCardReport(cashcard=[]):
	output = BytesIO()
	options = {'strings_to_numbers':True, 'default_date_format': 'mm/dd/yy', 'remove_timezone': True, 'in_memory': True}
	workbook = xlsxwriter.Workbook(output, options)
	worksheet = workbook.add_worksheet()
	worksheet.hide_gridlines(2)

	total = 0
	for line in cashcard:
		total = total + line[3]

	for r in range(7):
		worksheet.set_row(r, 22)

	worksheet.set_column('J:J',5)
	worksheet.set_column('K:K', 18)
	worksheet.set_column('L:L', 6)
	worksheet.set_column('M:M', 8)
	worksheet.set_column('N:N', 14)
	worksheet.set_column('O:O', 7.5)

	bold_format = workbook.add_format({'bold':1})
	bold_format.set_font_size(14)

	worksheet.set_column('A:A',7)
	worksheet.set_column('B:B', 18)
	worksheet.write_string('A1', 'Effective Date:', bold_format)
	worksheet.write_string('A2', 'Prepared by(source):', bold_format)
	worksheet.write_string('A3', 'Customer Profitability:', bold_format)

	date = datetime.now().strftime("%m/%d/%Y")
	num_date_format = workbook.add_format({'num_format':'mm/dd/yy', 'font_size': 12})
	border_format = workbook.add_format({'border': 1, 'align':'center', 'font_size': 12})
	num_date_with_format = workbook.add_format({'num_format':'mm/dd/yy', 'border': 1, 'align':'center', 'font_size': 12})

	worksheet.set_column('C:C', 16)
	worksheet.set_column('D:D', 5)
	worksheet.merge_range('C1:D1', date, num_date_with_format)
	worksheet.merge_range('C2:D2', 'JTR', border_format)
	worksheet.merge_range('C3:D3', 'N', border_format)

	money_format = workbook.add_format({'num_format':'#,##0.00', 'font_size':12, 'border':1, 'align':'center', 'valign':'center'})

	worksheet.set_column('E:E', 5)
	worksheet.set_column('F:F', 22)
	worksheet.write_string('C5', 'Total Debits:', bold_format)
	worksheet.write_string('C6', 'Total Credits:', bold_format)

	worksheet.write('F5', total/2.0, money_format)
	worksheet.write('F6', total/2.0, money_format)





	worksheet.set_column('G:G', 17)
	worksheet.set_column('H:H', 8)
	worksheet.write_string('G2', 'Introducing Broker:', bold_format)
	worksheet.write_string('G3', 'Batch Description:', bold_format)
	worksheet.write_string('G4', 'Client Number:', bold_format)

	client_num_format = workbook.add_format({'font_size':10, 'font_name': 'Courier', 'border':1, 'num_format':'000000000', 'align':'left'})

	worksheet.set_column('I:I', 50)
	worksheet.set_column('J:J', 5)
	worksheet.write('I2', '', client_num_format)
	worksheet.write('I3', '', client_num_format)
	worksheet.write('I4', 626996 , client_num_format)

	msg = "* 1st entry must be to a '9' account for customer profitability batches"
	msg_format = workbook.add_format({'font_size':14})
	worksheet.write('A7',msg, msg_format )

	header_format_r = workbook.add_format({'font_size':12, 'align':'center', 'valign':'vcenter', 'bg_color':'#CCCCCC', 'border':1})
	headers = ['Account', 'Cusip/Symbol', 'D/C', 'CCY', 'Amount', 'Shares', 'Code', 'Description', 'I/O', 'Contra Account', 'Office', 'Center','Cust/trader','Product']
	worksheet.set_row(7, 30)
	worksheet.write_row('B8', headers, header_format_r)

	header_format_c = workbook.add_format({'font_size':12, 'bg_color':'#CCCCCC', 'border':1, 'align':'left'})

	data_format = workbook.add_format({'font_size':10, 'border':1})
	amount_format = workbook.add_format({'font_size':10, 'border':1, 'num_format':'#,##0.00'})
	spaces = [''] * 6
	rows = len(cashcard)
	for r in range(rows):
		row = r + 8
		worksheet.set_row(row, 30)
		worksheet.write(row, 0, r+1, header_format_c)
		worksheet.write(row, 1, cashcard[r][0], data_format)
		worksheet.write(row, 2, '', data_format)
		worksheet.write(row, 3, cashcard[r][1], data_format)
		worksheet.write(row, 4, cashcard[r][2], data_format)
		worksheet.write(row, 5, cashcard[r][3], amount_format)
		worksheet.write(row, 6, '', data_format)
		worksheet.write(row, 7, cashcard[r][4], data_format)
		worksheet.write(row, 8, cashcard[r][5], data_format)
		worksheet.write_row('J'+str(row+1), spaces, data_format)


	workbook.close()
	output.seek(0)
	return output




if __name__ == '__main__':

	cashcard = [[u'ABCD5519', u'D', u'USD', 333.0, u'ACX', u'ASSOCI_JAN_17_GGGB'],
				[u'EFGH5519', u'D', u'USD', 234.0, u'ACX', u'ASSOCI_JAN_17_GGG'],
				[u'ABCD5519', u'C', u'USD', 333.0, u'ACT', u'ASSOCI_JAN_17_GGGB'],
				[u'ABCD5519', u'C', u'USD', 234.0, u'ACT', u'ASSOCI_JAN_17_GGG']]

	#getCashCardReport(cashcard)







