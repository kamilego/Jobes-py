import set_excel_hyperlink as seh
import os
import shutil

##############################
new_project = 'PUC2801'
new_date = '210407'
old_date = '210406'
##############################

old_main_proj = "Drawing5"
old_project = 'GDP0004B'
base_path = "D:\kamil"
dwg_dir = r"D:\kamil\_scripts\Drawing5.dwg"


newpath = '%s\%s' % (base_path, new_project)
if not os.path.exists(newpath):
    os.makedirs(newpath)
    shutil.copy(dwg_dir,"%s\%s\\" % (base_path, new_project))

# opening example file
b = open("D:\kamil\GDP0004B\GDP0004B.dsd")
a = b.readlines()
for i in range(len(a)):
    a[i] = a[i].replace(old_project, new_project).replace(old_date, new_date).replace(old_main_proj, new_project)

# creating .dsd file
f = open("%(x)s\%(y)s\%(y)s.dsd" % {"x": base_path, "y": new_project}, "w")
with f as filehandle:
    filehandle.writelines("%s" % elem for elem in a)

# creating .scr file
s = open("%s\%s\%s.scr" % (base_path, new_project, new_project), "w")
with s as filehandle:
    filehandle.writelines('(command "-PUBLISH" "%(x)s/%(y)s/%(y)s.dsd")\n' % {"x": base_path.replace("\\","/"), "y": new_project})

seh.create_excel_histry()
