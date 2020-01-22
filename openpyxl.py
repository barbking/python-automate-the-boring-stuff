import openpyxl
import os

os.chdir('C:\\Users\\barba\\Documents\\Automate_the_Boring_Stuff_2e_onlinematerials\\automate_online-materials')

workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.get_sheet_by_name('Sheet1')
print(workbook.get_sheet_names())