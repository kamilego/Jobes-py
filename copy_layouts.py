import shutil


def open_edit_txt(path):
    with open(path, "r") as f:
        read_data = f.readlines()
    read_data = [elem.split()[0] for elem in read_data][1:]
    read_data_split = []
    for elem in read_data:
        if not len(elem) > 8:
            read_data.append(elem.split("-")[0])
        else:
            read_data.append(elem[:-3])
    return read_data


def final_edit(read_data):
    read_data = set(read_data[:-7])
    tank_list = list(sorted(read_data, key=lambda x: int(x[2:])))
    tank_list.insert(13, "ZB-MOP-P")
    tank_list.insert(14, "ZB-MOP-L")
    script_list = []
    for elem in tank_list[::-1]:
        if elem == "ZB1":
            continue
        else:
            script_list.append(f"""(command "-layout" "copy" "Layout1 (3)" "{elem}")\n""")
    return script_list


def create_script_file(scripts_list, name):
    temp_path = r"P:\4861A2\5-WRK\5.4-OWN\05_SAN\11_ZBIORNIKI PPOŻ\skrypty\_template.scr"
    new_temp_path = temp_path.replace("_template", name)
    shutil.copy(temp_path, new_temp_path) 
    with open(new_temp_path , "w") as f:
        f.writelines(scripts_list)
        
def main():
    path = r"C:\Users\klegowicz\OneDrive - Multiconsult\Dokumenter\punkty.txt"
    a = open_edit_txt(path)
    b = final_edit(a)
    create_script_file(b, "layout_copy")
if __name__ == "__main__":
    main()
