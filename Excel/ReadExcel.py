from openpyxl import load_workbook

wb = load_workbook(filename = 'RACI.xlsx')

sheet_ranges = wb['Names on RACI']
print(sheet_ranges['C18'].value)




