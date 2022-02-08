import shutil

path = r"C:\Users\klegowicz\OneDrive - Multiconsult\Dokumenter\punkty.txt"

with open(path, "r") as f:
    b = f.readlines()
    
c = [elem.split()[0] for elem in b][1:]
h = []
for elem in c:
    if not len(elem) > 8:
        h.append(elem.split("-")[0])
    else:
        h.append(elem[:-3])

y = set(h[:-7])
t = list(sorted(y, key=lambda x: int(x[2:])))
t.insert(13, "ZB-MOP-P")
t.insert(14, "ZB-MOP-L")

r = []
for elem in t[::-1]:
    if elem == "ZB1":
        continue
    else:
        r.append(f"""(command "-layout" "copy" "Layout1 (3)" "{elem}")\n""")

def create_script_file(scripts_list, name):
    temp_path = r"P:\4861A2\5-WRK\5.4-OWN\05_SAN\11_ZBIORNIKI PPOŻ\skrypty\_template.scr"
    new_temp_path = temp_path.replace("_template", name)
    shutil.copy(temp_path, new_temp_path) 
    with open(new_temp_path , "w") as f:
        f.writelines(scripts_list)
        

create_script_file(r, "layout_copy")