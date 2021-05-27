from openpyxl import Workbook,load_workbook
from openpyxl.styles import PatternFill, Border, Side
from math import sqrt
import time
import codecs
import csv

begin_time = time.time()

def check_value(row):
    z = max(l[2] for l in row)
    k = min(l[2] for l in row)
    if abs(k) < abs(z):
        return str(row[0][0])+"_"+str(row[0][1]), round(z,2)
    else:
        return str(row[0][0])+"_"+str(row[0][1]), round(k,2)


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


path = r"D:\kamil\_scripts\pythony\zygry\fundamnety\fundamenty.csv"
path2 = path[:-3] + "xlsx"

with codecs.open(path,"rb","utf-16") as f:
    a = csv.reader(f,delimiter='\t')
    a = [''.join(elem) for elem in list(a)[1:]]

for i in range(len(a)):
    a[i] = change(a[i])
    a[i] = a[i].replace("(K)","").replace("\n","").replace("/",";").replace("KAM","/").split(";")


test = [a[i:13+i] for i in range(0,len(a),13)]

for i in range(len(test)):
    for elem in test[i]:
        if elem[2] == '-0,000':
            elem[2] = int(0)
        else:
            elem[2] = float(elem[2].replace(",","."))
        elem[0] = int(elem[0].strip())
        elem[1] = int(elem[1])
        elem[3] = float(elem[3].replace(",","."))
        elem[4] = float(elem[4].replace(",","."))
    test[i] = sorted(test[i], key=lambda x: x[1])

komb_set = set()

for elem in test:
    for row in elem:
        if row[1] not in komb_set:
            komb_set.add(row[1])
            
index_kom_set = [num for num in range(4,121)]            
a = []
for num in range(0,105,13):
	a.append(index_kom_set[num:num+13])

for step,elem in enumerate(a[1:],start=1):
	for num in range(len(elem)):
		elem[num] = elem[num] + step

indexes = [num for elem in a for num in elem]


komb_index = [(x,y) for x,y in zip(indexes,komb_set)]
fx = [elem[2] for num in range(len(test)) for elem in test[num]]
fy = [elem[3] for num in range(len(test)) for elem in test[num]]
fz = [elem[4] for num in range(len(test)) for elem in test[num]]
col_indexs = [num for elem in [indexes]*16 for num in elem]
row_ixdes = [[num]*117 for num in range(3,145,9)]
row_ixdes = [num for elem in row_ixdes for num in elem]
most_values = [(x,y,z,k,row) for x,y,z,k,row in zip(fx,fy,fz,col_indexs,row_ixdes)]


wb = load_workbook(r"D:\kamil\_scripts\pythony\zygry\fundamnety\fundamenty_temp.xlsx")
ws = wb.active

row1 = 2
for name in range(1,17):
    ws.cell(row1, 3).value = name
    cell_properties(ws.cell(row1, 3),"00C0C0C0")
    row1 += 9

for num in range(2,145,9):
    ws.cell(num,1).value = "FX"
    ws.cell(num+3,1).value = "FY"
    ws.cell(num+6,1).value = "FZ"
    
for row in range(2,145,3):
    for num, elem in komb_index:
        ws.cell(row, num).value = elem
            
for elem in most_values:
    ws.cell(elem[4],elem[3]).value = elem[0]
    ws.cell(elem[4]+3,elem[3]).value = elem[1]
    ws.cell(elem[4]+6,elem[3]).value = elem[2]


wb.save(r"D:\kamil\_scripts\pythony\zygry\fundamnety\fundamenty.xlsx")

