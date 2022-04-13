path = r"P:\4861A2\5-WRK\5.4-OWN\10_KON\EDIT\2.11B - ekrany przeciwolśnieniowe\wspolrzedne\NAZWY.csv"
new_path = path.replace("NAZWY", "NOWE")

with open(path, "r") as f:
    b = f.readlines()[1:]
    for i in range(len(b)):
        b[i] = b[i].replace("\n", "")
        b[i] = b[i].split(",")

a = [elem for elem in b if len(elem[0]) != 7]
c = [elem for elem in b if len(elem[0]) == 7]
right_list = c+a

main_dict = {f"{num}": [["PKT", "X", "Y"]] for num in range(1, 11)}

for elem in right_list:
    screen_num = int(elem[0].split(".")[0][2:])
    main_dict[f"{screen_num}"].append(elem)

for key, values in main_dict.items():
    sum1 = len([elem for elem in values if "a" in elem[0]])
    sum2 = len([elem for elem in values if "b" in elem[0]])
    print(f"Ekran: {key}, a:{sum1}, b:{sum2}, suma: {sum1+sum2}")

with open(new_path, "w") as f:
    for values in main_dict.values():
        for elem in values:
            f.writelines(",".join(elem)+"\n")
            
