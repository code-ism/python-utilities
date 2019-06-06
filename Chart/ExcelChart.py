import xlsxwriter

workbook = xlsxwriter.Workbook('ChartDemo.xlsx')
worksheet = workbook.add_worksheet()

keys = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
data = [3,4,6,8,12,15,17,17,15,11,7,4]
worksheet.write_column('A1', keys)
worksheet.write_column('B1', data)
chart = workbook.add_chart({'type' : 'column'})
chart.set_title({'name' : 'Weather Averages, Amsterdam'})
chart.add_series({'name' : 'Temperature(°C)',
                'categories' : 'Sheet1!$A$1:$A12',
                'values' : 'Sheet1!$B$1:$B12',
                'data_labels' : {'value' : True}
                })
worksheet.insert_chart('D2', chart)
workbook.close()
