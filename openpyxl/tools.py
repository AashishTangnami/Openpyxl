import openpyxl as xl

class Excel_tools:    
    def countRow (fileName,sheetName):
        wb = xl.load_workbook(fileName)
        sheet = wb.get_sheet_by_name(sheetName)
        return (sheet.max_row)
    #returns the total number of rows present in that particular sheet of excel file
    def countColumn (fileName,sheetName):
        wb = xl.load_workbook(fileName)
        sheet = wb.get_sheet_by_name(sheetName)
        return (sheet.max_column)
    #returns the total number of columns present in that particular sheet of excel file
    def readData (fileName,sheetName,rowN,columnN):
        wb = xl.load_workbook(fileName)
        sheet = wb.get_sheet_by_name(sheetName)
        return (sheet.cell(row=rowN, column=columnN)).value
    #returns the data present in the cell of those particular sheets of given row and given column

        

