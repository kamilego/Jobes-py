from openpyxl.utils import get_column_letter

# konrektne komórki z innego sheeta
for num in range(5,7*4,4):
	for elem in range(4,4+13*9,13):
		print(f"=Arkusz1!{get_column_letter(elem)}{num}")

# grupa komórek z innego sheeta	
for num in range(3,114*3,9):
	print(f"=MIN(Sheet!B{num}:B{num+9})")

a = 40
while a >2:
	print(f"=M{a}")
	a -= 1

# tworzenie ciągu przypadków dziłajacych kombinacji na konkrenty pręt
def list_func(range1, range2, step):
	compre = [num for num in range(range1,range2,step)]
	compre = compre[:3] + compre[6:]
	return compre

a1 = list_func(102,234,11)
a2 = list_func(112,244,11)

for num in range(1,14):
	for x,y in zip(a1, a2):
		print(f"{num}_{x}-{y}")