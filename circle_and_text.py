import shutil


def create_script_list(data):
    script_list = []
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "").split(" ")
        data[i] = [data[i][0]]+data[i][-2:]
        data[i][1] = data[i][1][data[i][1].index(";")+3:-1]
        data[i][2] = data[i][2].replace("}", "")[2:]
        script_list.append(f"""(command "circle" "{data[i][2]},{data[i][1]}" "1.5")\n""")
        script_list.append(f"""(command "_TEXT" "{data[i][2]},{data[i][1]}" "2" "0" "{data[i][0][-1]}")\n""")
    script_list[-1] = script_list[-1].replace("\n", "")
    return script_list


def create_script_file(scripts_list, name):
    temp_path = r"P:\4861A2\5-WRK\5.4-OWN\05_SAN\11_ZBIORNIKI PPOŻ\skrypty\_template.scr"
    new_temp_path = temp_path.replace("_template", name)
    shutil.copy(temp_path, new_temp_path) 
    with open(new_temp_path , "w") as f:
        f.writelines(scripts_list)


def load_data(path):
    with open(path, "r") as f:
        a = f.readlines()
        script_list = create_script_list(a)
    return script_list


def main():
    path = r"P:\4861A2\5-WRK\5.4-OWN\05_SAN\11_ZBIORNIKI PPOŻ\skrypty\coord_export.txt"
    name = "circle_and_text"
    data = load_data(path)
    create_script_file(data, name)
if __name__ == '__main__':
    main()
