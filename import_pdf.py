import shutil
import os


def print_func(path, coord):
    text = f"""-PDFATTACH

"{path}"
1
{coord[0]:.4f},{coord[1]:.4f}
1
0
"""
    return text


def create_scripts_list(path, coord=[328.294, 703.1181], coord_zb2=[328.294, 303.1181]):
    pdfs_name = os.listdir(path)
    combined_elems = []
    for name in pdfs_name:
        path_join = os.path.join(path, name)
        if "ZB2" in name:
            combined_elems.append(print_func(path_join, coord_zb2))
            coord_zb2[0] += 500
            if coord_zb2[0] == 328.294+500:
                coord[1] -= 400
        else:
            combined_elems.append(print_func(path_join, coord))
            coord[1] -= 400
    return combined_elems


def create_script_file(scripts_list, name):
    temp_path = r"P:\4861A2\5-WRK\5.4-OWN\05_SAN\11_ZBIORNIKI PPOŻ\skrypty\_template.scr"
    new_temp_path = temp_path.replace("_template", name)
    shutil.copy(temp_path, new_temp_path) 
    with open(new_temp_path , "w") as f:
        f.writelines(scripts_list)


def main():
    path = r"Z:\XX_WYMIANA_temp\Kamil L\pdfy"
    name = "pdf_import"
    script_list = create_scripts_list(path)
    create_script_file(script_list, name)
if __name__ == '__main__':
    main()
