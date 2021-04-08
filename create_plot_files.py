import set_excel_hyperlink as seh
import os
import shutil

# Can be changed:
##############################
new_project = 'WLO0302A'                            # brand new name for the project
new_date = '210210'                                 # date which appears in AutoCAD in layouts names
old_date = '210407'                                 # date which appears in .dsd file - probably not to change
new_rev_1 = "REW.01"                                # new revision num - full version PS_e, PS01, T01 & T02
new_rev_2 = "REW.02"                                # new revision num - shorter version T01 & T02
##############################

# Cannot be changed:
old_project = 'GDP0004B'                            # old name project which is a template name
old_rev_1 = "REW.03"                                # revision num for PS_e, PS01, T01 & T02 - full version
old_rev_2 = "REW.04"                                # revision num fo T01 & T02 - shorter version
old_main_proj = "Drawing5"
base_path = "D:\kamil"
dwg_dir = "D:\kamil\_scripts\Drawing5.dwg"

dic_w_replace = {old_project: new_project,
                 old_date: new_date, 
                 old_rev_1: new_rev_1, 
                 old_rev_2: new_rev_2}

newpath = '%s\%s' % (base_path, new_project)
if not os.path.exists(newpath):
    os.makedirs(newpath)
    shutil.copy(dwg_dir,"%s\%s\\" % (base_path, new_project))

# opening example file
b = open(r"D:\kamil\_scripts\template.dsd")
a = b.readlines()
for i in range(len(a)):
    for key, value in dic_w_replace.items():
        a[i] = a[i].replace(key, value)

# creating .dsd file
f = open("%(x)s\%(y)s\%(y)s.dsd" % {"x": base_path, "y": new_project}, "w")
with f as filehandle:
    filehandle.writelines("%s" % elem for elem in a)

# creating .scr file
s = open("%(x)s\%(y)s\%(y)s.scr" % {"x": base_path, "y": new_project}, "w")
with s as filehandle:
    filehandle.writelines('(command "-PUBLISH" "%(x)s/%(y)s/%(y)s.dsd")\n' % {"x": base_path.replace("\\","/"), "y": new_project})
