import openpyxl as xl
from tools import Excel_tools

class Excel(object):    
    def __init__(self):                
        excel_path = "FormatforFinancial_Reporting.xlsx" #path of the excel file
        wb = xl.load_workbook(excel_path) #loads the excel file as wb (workbook)
        sheet = []
        sheet = wb.sheetnames
        i = 0
        for i in range(len(sheet)):
            sheets = sheet[i]
            row = Excel_tools.countRow(excel_path, sheets) #returns the total number of rows of that particular sheet
            col = Excel_tools.countColumn(excel_path, sheets) #returns the total number of column of that particular sheet

            for dataC in range(1, col + 1):
                k= []
                v= []
                for dataR in range(1, row + 1):
                    if Excel_tools.readData(excel_path, sheets, dataR, 2) is None:
                        continue
                    else:
                        key = Excel_tools.readData(excel_path, sheets, dataR, 2) #returns all the row's value of column 2
                    if Excel_tools.readData(excel_path, sheets, dataR, 4) is None:
                        continue
                    else:
                        value = Excel_tools.readData(excel_path, sheets, dataR, 4) #returns all the row's value of column 4
                    k.append(key)
                    v.append(value)
            if sheets == sheet[0]:
                continue #ignoring first sheet

            d ={ k[i]: v[i] for i in range(len(k)) } #converting two list k and v into dictionary for key value pairs
            
            if sheets == sheet[1]:
                self.liability = sum(d.values())
                # array['liability'] = liability
                # print('liability :',liability)
            if sheets == sheet[2]:
                self.assets = sum(d.values())
                # array['assets']=assets
                # print('Assets :',assets)
            if sheets == sheet[3]:
                self.income = sum(d.values())
                # array['income']=income
                # print('Income :',income)
            if sheets == sheet[4]:
                self.expenses = sum(d.values())
                # array['expenses']=expenses
                # print('Expenses :',expenses)
        



