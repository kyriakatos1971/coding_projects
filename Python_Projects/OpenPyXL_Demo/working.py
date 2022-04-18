from openpyxl import Workbook, load_workbook



wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append(['This','is','an','openpyxl','demo'])

wb.save('Demo.xlsx')

