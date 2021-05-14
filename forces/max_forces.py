import csv
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Fill, PatternFill, colors, Border, Side, Font, Alignment
import string
from math import sqrt


def asd(row):
    z = max(l[3] for l in row)
    k = min(l[3] for l in row)
    if abs(k) < abs(z):
        return str(row[0][2])+"_"+str(row[0][0]), round(z,2)
    else:
        return str(row[0][2])+"_"+str(row[0][0]), round(k,2)


def change(elem):
    if elem.count("/") == 3:
        pos = elem.index('/', elem.index('/') + 1)
        elem = elem[:pos] + 'KAM' + elem[pos + 1:]
    return elem


def cell_properties(cell,color):
    y = cell
    y.fill = PatternFill(fgColor=color, fill_type = "solid")
    thin = Side(border_style="thin", color="000000")
    y.border = Border(top=thin, left=thin, right=thin, bottom=thin)


def cells_range(rowik, a,b):
    sum_val = 0
    for num in range(a,b):
        sum_val += (ws.cell(rowik, num).value)**2
    return round(sqrt(sum_val),2)


def sumq(row, value):
    ws.cell(row, value).value = cells_range(row, value+1, value+13)
    cell_properties(ws.cell(row, value),"00FF6600")


def max_force(row):
    ws.cell(row,2).value = max(ws.cell(row-1,3).value + ws.cell(row,3).value,ws.cell(row-1,16).value + ws.cell(row,16).value,ws.cell(row-1,29).value + ws.cell(row,29).value)
    cell_properties(ws.cell(row, 2),"00008000")


with open(r"D:\kamil\RTON Kisielice\cs2.txt", "r") as a:
    a = a.readlines()

for i in range(len(a)):
    a[i] = change(a[i])
    a[i] = a[i].replace("(K)","").replace("\n","").replace("/",";").replace("KAM","/").split(";")
del a[0]

test = [a[i:975+i] for i in range(0,len(a),975)]
all_list = []

for i in range(len(test)):
    test[i] = sorted(test[i], key=lambda x: x[2])
    for elem in test[i]:
        elem[0] = int(elem[0].strip())
        elem[2] = int(elem[2])
        elem[3] = float(elem[3].replace(",","."))

all_list = []

for elem in test:
    for num in range(0,975,25):
        all_list.append(elem[num:num+25])

diction ={}

for row in all_list:
    diction[asd(row)[0]] = asd(row)[1]

prety = sorted(set([int(elem[3:]) for elem in list(diction.keys())]))
kombinacje = sorted(set([elem[:2] for elem in list(diction.keys())]))

wb = Workbook()
ws = wb.active

row1 = 3
num1 = 2
for name in prety:
    ws.cell(row1, num1).value = name
    cell_properties(ws.cell(row1, num1),"00C0C0C0")
    row1 += 3

for ami in range(0,len(diction.values()),39):
    for to in range(3,len(prety)*3+1,3):
        for ro in range(3,len(kombinacje)+3):
            if to == int(ami/13)+3:
                ws.cell(to, ro).value = list(diction.values())[ro+ami-3]
                cell_properties(ws.cell(to, ro),"00FFCC99")
            
for to in range(2,len(prety)*3+2,3):
    for ro in range(3,len(kombinacje)+3):
        ws.cell(to, ro).value = list(diction.keys())[ro-3][:2]
        cell_properties(ws.cell(to, ro),"00666699")
    for num in range(4,16):
        ws.cell(to+2, num).value = ws.cell(to+1, 3).value - ws.cell(to+1, num).value
    for num in range(17,29):
        ws.cell(to+2, num).value = ws.cell(to+1, 16).value - ws.cell(to+1, num).value
    for num in range(30,42):
        ws.cell(to+2, num).value = ws.cell(to+1, 29).value - ws.cell(to+1, num).value
    for num in range(3,30,13):
        sumq(to+2,num)
    max_force(to+2)

list_of_values = []

ws2 = wb.create_sheet("Segmenty")
for num in range(3,len(prety)*3+2,9):
    list_of_values.append(max(ws.cell(num+1,2).value, ws.cell(num+4,2).value, ws.cell(num+7,2).value))

elem_max = max(list_of_values)
ws2.cell(2,7).value = "Segment"
ws2.cell(2,8).value = "Wartość"
for row in range(3,33):
    ws2.cell(row,7).value = row-2
    ws2.cell(row,8).value = list_of_values[row-3]
    cell_properties(ws2.cell(row, 8),"00FFFFFF")
    cell_properties(ws2.cell(row, 7),"00FFFFFF")
    if row-3 == list_of_values.index(elem_max):
        cell_properties(ws2.cell(row, 8),"00FF6600")

wb.save(r"D:\kamil\RTON Kisielice\Nowy Arkusz programu Microsoft Excel.xlsx")
