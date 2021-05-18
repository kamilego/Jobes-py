import os
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side


def cell_properties(cell,color):
    y = cell
    y.fill = PatternFill(fgColor=color, fill_type = "solid")
    thin = Side(border_style="thin", color="000000")
    y.border = Border(top=thin, left=thin, right=thin, bottom=thin)


path = r"D:\kamil\RTON Kisielice\new"
fil_csv = os.listdir(path)

blank_list = [os.path.join(path,elem) for elem in fil_csv]
results = []

for elem in blank_list:
    with open(elem) as r:
        a = r.readlines()[1:]
        results.append(a)

new_results = []

for elem in results:
    for i in range(len(elem)):
        elem[i] = elem[i].replace("\n", "")
        elem[i] = elem[i].replace(",", ".")
        elem[i] = elem[i].replace("/", ";")
        elem[i] = elem[i].split(";")
        elem[i][0] = int(elem[i][0].strip())
        elem[i][1] = int(elem[i][1].strip())
        elem[i][2] = float(elem[i][2])
        new_results.append(elem[i])

results = [new_results[i:13+i] for i in range(0,len(new_results),13)]

elem_names = []
komb_num = []

for elem in results:
    for num in range(len(elem)):
        if elem[num][0] not in elem_names: 
            elem_names.append(elem[num][0])
        if elem[num][1] not in komb_num:
            komb_num.append(elem[num][1])


wb = Workbook()
ws = wb.active

row1 = 3
num1 = 2
for name in elem_names:
    ws.cell(row1, num1).value = name
    cell_properties(ws.cell(row1, num1),"00C0C0C0")
    row1 += 3

step = 0


for row in range(2,len(elem_names)*3,3):
    for num in range(3,len(komb_num)+3):
        ws.cell(row, num).value = komb_num[num-3]
        ws.cell(row+1, num).value = new_results[step][2]
        step += 1

    
wb.save(r"D:\kamil\RTON Kisielice\asd.xlsx")

