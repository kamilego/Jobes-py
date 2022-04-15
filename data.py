def create_list_from_data(path: str) -> list:
    with open(path, "r") as f:
        b = f.readlines()[1:]
        for i in range(len(b)):
            b[i] = b[i].replace("\n", "")
            b[i] = b[i].split(",")
    a = [elem for elem in b if len(elem[0]) != 7]
    c = [elem for elem in b if len(elem[0]) == 7]
    right_list = c+a
    return right_list
    
def modify_list(data_list: list) -> dict:
    main_dict = {f"{num}": [["PKT", "X", "Y"]] for num in range(1, 11)}
    for elem in data_list:
        screen_num = int(elem[0].split(".")[0][2:])
        main_dict[f"{screen_num}"].append(elem)
    for key, values in main_dict.items():
        sum1 = len([elem for elem in values if "a" in elem[0]])
        sum2 = len([elem for elem in values if "b" in elem[0]])
        print(f"Ekran: {key}, a:{sum1}, b:{sum2}, suma: {sum1+sum2}")
    return main_dict
    
def save_file(new_path: str, modified_dict: dict) -> None:
    with open(new_path, "w") as f:
        for values in modified_dict.values():
            for elem in values:
                f.writelines(",".join(elem)+"\n")
            
def main():
    path = r"P:\4861A2\5-WRK\5.4-OWN\10_KON\EDIT\2.11B - ekrany przeciwolśnieniowe\wspolrzedne\NAZWY.csv"
    new_path = path.replace("NAZWY", "NOWE")
    created_list = create_list_from_data(path)
    modified_dict = modify_list(created_list)
    save_file(new_path, modified_dict)
if __name__ == "__main__":
    main()
