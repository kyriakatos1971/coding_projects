import os
import xlrd
import xlsxwriter


# Create a demo XL
wbk = xlsxrwriter.Workbook('TEST.xlsx')
wks = wbk.add_worksheet()
i = -1

for x in range(1,1000,11):
    i+=1
    cella = xl_rowcol_to_cell(i,0)
    cellb = xl_rowcol_to_cell(i,1)
    cellc = xl_rowcol_to_cell(i,2)
    print(cella)
    wks.write(cella,x)
    wks.write(cellb,x*3)
    wks.write(cellc,x*4.5)
myPath = r'C:\Desktop\Test.xslx'
wbk.close()

