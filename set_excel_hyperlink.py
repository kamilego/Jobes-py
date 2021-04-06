import os
import xlsxwriter
def create_excel_histry():
    lista = (os.listdir('D:/kamil/'))
    del lista[0:2]
    del lista[-3:-1]
    lista.remove("historia.xlsx")
    lista = lista[0:len(lista)-1]
    workbook = xlsxwriter.Workbook("D:\kamil\historia.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.set_column('C:C', 10)
    for num, elem in enumerate(lista, start = 5):
        worksheet.write_url("C"+str(num), 'external:D:/kamil/'+elem, string = elem)
    workbook.close()
