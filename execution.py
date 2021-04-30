from prepare_new_project import NewProject


new_project = 'OTS3301A'                                   # brand new name for the project
new_date = '210430'                                        # date which appears in AutoCAD in layouts names
new_rev_1 = "REW.01"                                       # new revision num - full version PS_e, PS01, T01 & T02
new_rev_2 = "REW.02"                                       # new revision num - shorter version T01 & T02

lok1 = "Wieża BOT-E3/54 wys. całkowita 55,95m n.p.t."
lok2 = "77-131 Płotowo, ID działki 220102_5.0007.161"


b = NewProject(new_project, new_date, new_rev_1, new_rev_2, lok1, lok2)
b.execution()
b.first_steps()
b.create_excel_histry()
