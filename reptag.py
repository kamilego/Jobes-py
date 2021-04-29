import re
import os
import datetime


class ChangeTags:
    date = datetime.datetime.now().isoformat()[:10]
    path = r"D:\kamil\_scripts\templates\tagi.SCR"
    def __init__(self, project_name, lok1, lok2):
        self.project_name = project_name
        self.lok1 = lok1
        self.lok2 = lok2


    def check_platform(self, tower):
        if "E2" in tower:
            return "PRM-B2.35"
        elif "E3" in tower:
            return "PRM-B3.35"
        else:
            return "PRM-B4.35"


    def execution(self):
        area = self.lok2[self.lok2.index(".",self.lok2.index(".")+1)+1:]
        tower_type = re.compile(r'E\d/\d\d').findall(self.lok1)[0]
        platform_type = check_platform(tower_type)
        list_values = [self.project_name, date, self.lok1, self.lok2, area, tower_type, platform_type]

        a = open(r"D:\kamil\_scripts\templates\tagi.SCR")
        a = a.readlines()

        num_list = [elem for elem in range(10,len(a),12)]
        dictionary = {key: value for key, value in zip(num_list, list_values)}

        for key, value in dictionary.items():
            a[key] = value + "\n"

        with open(os.path.join("D:\kamil",self.project_name.replace(" ",""),"tagi.scr"), "w") as g:
            g.writelines("%s" % elem for elem in a)

project_name = "BTW 3201 A"
lok1 = "Wieża BOT-E3/54 wys. całkowita 55,95m n.p.t."
lok2 = "77-131 Płotowo, ID działki 220102_5.0007.161"

a = ChangeTags(project_name, lok1, lok2)
a.execution()
