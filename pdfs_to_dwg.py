import shutil
import os

def print_func(path, coord):
    text = f"""-pdfimport

"{path}"
1
{coord[0]:.4f},{coord[1]:.4f}
1
0
"""
    return text

path_pdfs = r"Z:\XX_WYMIANA_temp\Kamil L\pdfy"
coord = [2260.8481, 205.8158]

pdfs_name = os.listdir(path_pdfs)
not_mop_list = [elem for elem in pdfs_name if "MOP" not in elem]
mop_list = [elem for elem in pdfs_name if "MOP" in elem]
pdfs_name = not_mop_list + sorted(mop_list, reverse=True)

combined_elems = []
for path in pdfs_name:
        combined_elems.append(print_func(os.path.join(path_pdfs, path), coord))
        coord[1] += 700

temp_path = r"P:\4861A2\5-WRK\5.4-OWN\05_SAN\11_ZBIORNIKI PPOŻ\skrypty\_template.scr"
new_temp_path = temp_path.replace("_template", "_template_new")
shutil.copy(temp_path, new_temp_path) 

with open(new_temp_path , "w") as f:
    f.writelines(combined_elems)
