import set_excel_hyperlink as seh

# Can be changed:
##############################
new_project = 'OOT9011A'                               # brand new name for the project
new_date = '210420'                                        # date which appears in AutoCAD in layouts names
new_rev_1 = "REW.01"                                       # new revision num - full version PS_e, PS01, T01 & T02
new_rev_2 = "REW.02"                                       # new revision num - shorter version T01 & T02
##############################

# Cannot be changed:
old_date = '210402'                                        # date which appears in .dsd file - probably not to change
old_project = 'GDP0004B'                                   # old name project which is a template name
old_rev_1 = "REW.01"                                       # revision num for PS_e, PS01, T01 & T02 - full version
old_rev_2 = "REW.02"                                       # revision num fo T01 & T02 - shorter version
old_main_proj = "Drawing5"
dwg_dir = r"D:\kamil\_scripts\templates\Drawing5.dwg"      # path where is example file with all prepared blocks
xlsx_path = r"D:\kamil\_scripts\templates\KALKULATOR_KK_nieghaslo.xlsx"
base_path = dwg_dir[:8]

dic_w_replace = {old_project: new_project,
                 old_date: new_date, 
                 old_rev_1: new_rev_1, 
                 old_rev_2: new_rev_2}

seh.first_steps(base_path, new_project, dwg_dir, xlsx_path, dic_w_replace)
fold_list = seh.list_of_folders()
seh.create_excel_histry(fold_list)
seh.edit_excel_histry(fold_list)
