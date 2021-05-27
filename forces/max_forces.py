from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side
from math import sqrt
import time
import codecs
import csv

begin_time = time.time()

def check_value(row):
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
    ws.cell(row, value+1).value = cells_range(row, value+2, value+14)
    cell_properties(ws.cell(row, value+1),"00FF6600")


def minus_value_check(row, col):
    if ws.cell(row,col+1).value < 0:
        return ws.cell(row,col+1).value - ws.cell(row+1,col+1).value
    else:
        return ws.cell(row,col+1).value + ws.cell(row+1,col+1).value


def list_check(lis):
    if len([elem for elem in lis if elem < 0]) == 9:
        return lis[::-1]
    else:
        return lis


def max_force(row,col, a):
    val_list = []
    for num in range(3,29*4,13):
        val_list.append(minus_value_check(row-1,num))
    val_list = sorted(val_list)
    val_list = list_check(val_list)
    if a == 1:  
        value = val_list[-1]
    else:
        value = val_list[0]
    ws.cell(row, col).value = value
    cell_properties(ws.cell(row, col),"00008000")


path = r"D:\kamil\_scripts\pythony\zygry\krawezniki\krawezniki.csv"
path2 = path[:-3] + "xlsx"

with codecs.open(path,"rb","utf-16") as f:
    a = csv.reader(f,delimiter='\t')
    a = [''.join(elem) for elem in list(a)[1:]]

for i in range(len(a)):
    a[i] = change(a[i])
    a[i] = a[i].replace("(K)","").replace("\n","").replace("/",";").replace("KAM","/").split(";")
a = [row[:4] for row in a]

for num in range(len(a)):
    for i in range(2):
        a[num][i] = a[num][i].strip()
    a[num][0] = int(a[num][0])
    a[num][2] = int(a[num][2])
    a[num][3] = float(a[num][3].replace(",","."))

a = sorted(a, key=lambda x: x[2])


all_list = [a[num:num+10] for num in range(0,len(a),10)]



diction ={}

for row in all_list:
    diction[check_value(row)[0]] = check_value(row)[1]

aa = {}

for elem in range(458):
	for num in range(0,len(diction),458):
		aa[list(diction.keys())[elem+num]] = diction[list(diction.keys())[elem+num]]

prety = sorted(set([int(elem.split("_")[1]) for elem in list(aa.keys())]))
kombinacje = sorted(set([int(elem.split("_")[0]) for elem in list(aa.keys())]))

wb = Workbook()
ws = wb.active

row1 = 3
num1 = 3
for name in prety:
    ws.cell(row1, num1).value = name
    cell_properties(ws.cell(row1, num1),"00C0C0C0")
    row1 += 3

for row in range(2,len(prety)*3,3):
    for num, name in enumerate(kombinacje,start=4):
        ws.cell(row, num).value = name
        cell_properties(ws.cell(row, num),"00666699")
ami = 0
for to in range(3,len(prety)*3+1,3):
    for ro in range(4,len(kombinacje)+4):
        ws.cell(to, ro).value = list(aa.values())[ami]
        cell_properties(ws.cell(to, ro),"00FFCC99")
        ami+=1


for to in range(2,len(prety)*3+2,3):
    for num in range(5,17):
        ws.cell(to+2, num).value = ws.cell(to+1, 4).value - ws.cell(to+1, num).value
    for num in range(18,30):
        ws.cell(to+2, num).value = ws.cell(to+1, 17).value - ws.cell(to+1, num).value
    for num in range(31,43):
        ws.cell(to+2, num).value = ws.cell(to+1, 30).value - ws.cell(to+1, num).value
    for num in range(44,56):
        ws.cell(to+2, num).value = ws.cell(to+1, 43).value - ws.cell(to+1, num).value
    for num in range(57,69):
        ws.cell(to+2, num).value = ws.cell(to+1, 56).value - ws.cell(to+1, num).value
    for num in range(70,82):
        ws.cell(to+2, num).value = ws.cell(to+1, 69).value - ws.cell(to+1, num).value
    for num in range(83,95):
        ws.cell(to+2, num).value = ws.cell(to+1, 82).value - ws.cell(to+1, num).value
    for num in range(96,108):
        ws.cell(to+2, num).value = ws.cell(to+1, 95).value - ws.cell(to+1, num).value
    for num in range(109,121):
        ws.cell(to+2, num).value = ws.cell(to+1, 108).value - ws.cell(to+1, num).value
    for num in range(3,120,13):
        sumq(to+2,num)
    max_force(to+2, 2, 0)
    max_force(to+2, 1, 1)


ws2 = wb.create_sheet("Segmenty")
ws2.cell(2,5).value = "Plusy"
ws2.cell(2,6).value = "Minusy"
ws2.cell(2,7).value = "Segment"
ws2.cell(2,8).value = "Wartość"
ws2.cell(2,9).value = "Wytężenie"

for num in range(3,49):
    ws2.cell(num,7).value = num-2

a12 = [num for num in range(38,1064,27)]
"=MAX(Sheet!B1:B46)"
for num, val in enumerate(a12,start=4):
    ws2.cell(num,5).value = f"=MAX(Sheet!A{val}:A{val+27})"
    ws2.cell(num,6).value = f"=MIN(Sheet!B{val}:B{val+27})"

a22 = [num for num in range(1064,1352+16*3,16*3)]
for num, val in enumerate(a22,start=42):
    ws2.cell(num,5).value = f"=MAX(Sheet!A{val}:A{val+48})"
    ws2.cell(num,6).value = f"=MIN(Sheet!B{val}:B{val+48})"   

ws2.cell(3,5).value = f"=MAX(Sheet!A3:A37)"
ws2.cell(3,6).value = f"=MIN(Sheet!B3:B37)"



wb.save(path2)


print(round(time.time() - begin_time,2))


