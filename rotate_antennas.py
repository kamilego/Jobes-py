import pyautogui
import time
import math
from math import *

begin_time = time.time()

# to be changed
a1 = [95, 0.6, 1]
a2 = [226, 0.6, 2]
a3 = [103, 0.6, 3]
a4 = [150, 0.6, 4]
a5 = [189, 0.6, 5]
a6 = [250, 0.6, 6]

tow_check_E = "E2"      # E2 or E3 # note that: E4 == E3
tow_azimuth = 21
speed = 0
# to be changed end

# todo 2: try to split function that counts new rotated coordinates

# mouse location
# once set always will work
mid_w1_pos = [828, 366]
mid_w2_pos = [1139, 366]
prop_visib_pos = [1753, 733]
arrow_red_pos = [1289, 813]
cross_ant_local = [160, 304]
all_a = [a1, a2, a3, a4, a5, a6]


def tower_type(tow_check):
    if tow_check == "E2":
        return [0, 0, 0]
    elif tow_check == "E3":
        return [16, 12, 8]


w1 = {"left": [mid_w1_pos[0] - (45 + tower_type(tow_check_E)[1]), mid_w1_pos[1] + (24 + tower_type(tow_check_E)[2])],
      "right": [mid_w1_pos[0] + (45 + tower_type(tow_check_E)[1]), mid_w1_pos[1] + (24 + tower_type(tow_check_E)[2])],
      "middle": [mid_w1_pos[0], mid_w1_pos[1] - (51 + tower_type(tow_check_E)[0])]}
w2 = {"left": [mid_w2_pos[0] - (45 + tower_type(tow_check_E)[1]), mid_w2_pos[1] + (24 + tower_type(tow_check_E)[2])],
      "right": [mid_w2_pos[0] + (45 + tower_type(tow_check_E)[1]), mid_w2_pos[1] + (24 + tower_type(tow_check_E)[2])],
      "middle": [mid_w2_pos[0], mid_w2_pos[1] - (51 + tower_type(tow_check_E)[0])]}
prop_below_vis_pos = [prop_visib_pos[0], prop_visib_pos[1] + 19]
ant_green_pos = [arrow_red_pos[0], arrow_red_pos[1] - 113]
offset_arrow_red = [arrow_red_pos[0] - 357, arrow_red_pos[1]]
# mouse location end


def visibility(elem):
    if elem == 0.3:
        pyautogui.press("enter")
    elif elem == 0.6:
        pyautogui.typewrite('0')
    else:
        pyautogui.typewrite('1')


def degree_change(azimuth):
    if azimuth < 180:
        return 180
    else:
        return 0


def rot_position(azimuth, poz1, poz2, az_rot = 0):
    alfa = azimuth - az_rot - 90
    cos_alfa = math.cos(math.radians(alfa))
    sin_alfa = math.sin(math.radians(alfa))
    l = sqrt((poz1[0] - poz2[0]) ** 2 + (poz1[1] - poz2[1]) ** 2)
    x1 = poz1[0] + l * cos_alfa
    y1 = poz1[1] + l * sin_alfa
    return x1, y1


def sort_az_list():
    azimuths = [a2, a3, a4, a5, a6]
    az_list1 = [a1]
    az_list2 = []
    for elem in azimuths:
        if not len(az_list1) == 3:
            if 30 < abs(elem[0] - az_list1[0][0]) < 150 or 210 < abs(elem[0] - az_list1[0][0]) < 330:
                az_list1.append(elem)
            else:
                az_list2.append(elem)
        else:
            az_list2.append(elem)
    return az_list1, az_list2


def azimuth_check(az):
    if az < 120:
        return az
    elif 120 <= az < 240:
        return az - 120
    else:
        return az - 240


def antennas_pos_w(ant_azimuth, tow_az, tower):
    if 300 <= ant_azimuth[0] <= 360 or 0 <= ant_azimuth[0] <= 60:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antennas_positions(tower["middle"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antennas_positions(tower["left"], azimuth_check(tow_az))
    if 60 < ant_azimuth[0] < 180:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antennas_positions(tower["right"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antennas_positions(tower["middle"], azimuth_check(tow_az))
    if 180 <= ant_azimuth[0] < 300:
        if 300 <= azimuth_check(tow_az) <= 360 or 0 <= azimuth_check(tow_az) <= 60:
            return new_rotated_antennas_positions(tower["left"], azimuth_check(tow_az))
        elif 60 < azimuth_check(tow_az) <= 120:
            return new_rotated_antennas_positions(tower["right"], azimuth_check(tow_az))


def new_rotated_antennas_positions(elem, az):
    if elem == w1["left"]:
        return rot_position(az, mid_w1_pos, elem, az_rot = 120)
    elif elem == w1["right"]:
        return rot_position(az, mid_w1_pos, elem, az_rot = 240)
    elif elem == w1["middle"]:
        return rot_position(az, mid_w1_pos, elem, az_rot = 0)
    elif elem == w2["left"]:
        return rot_position(az, mid_w2_pos, elem, az_rot = 120)
    elif elem == w2["right"]:
        return rot_position(az, mid_w2_pos, elem, az_rot = 240)
    elif elem == w2["middle"]:
        return rot_position(az, mid_w2_pos, elem, az_rot = 0)


def rotate(az, visib, lok):
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.click(prop_visib_pos)
    visibility(visib[1])
    pyautogui.click(prop_below_vis_pos)
    pyautogui.typewrite(str(az[0]))
    pyautogui.press("enter")
    pyautogui.typewrite(str(az[2]))
    pyautogui.press("enter")
    pyautogui.typewrite(str(degree_change(az[0])))
    pyautogui.press("enter")
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.click()
    pyautogui.click(offset_arrow_red, duration=speed)
    pyautogui.moveTo(mid_w1_pos, duration=speed)
    pyautogui.click()
    pyautogui.moveTo(mid_w2_pos, duration=speed)
    pyautogui.click()
    pyautogui.moveTo(rot_position(az[0], arrow_red_pos, ant_green_pos)[0] - (arrow_red_pos[0] - offset_arrow_red[0]),
                     rot_position(az[0], arrow_red_pos, ant_green_pos)[1], duration=speed)
    pyautogui.click()
    pyautogui.press("f3")
    pyautogui.moveTo(lok, duration=speed)
    pyautogui.click()
    pyautogui.press("f3")
    pyautogui.press("esc")


def towers_rotate(tow_az, tow_check):
    pyautogui.click()
    pyautogui.click(mid_w1_pos, duration=speed)
    pyautogui.click(mid_w2_pos, duration=speed)
    if tow_check == "E3":
        pyautogui.click(prop_visib_pos)
        pyautogui.typewrite("e")
    if not tow_az == 0:
        pyautogui.click(prop_below_vis_pos)
        pyautogui.typewrite(str(tow_az))
        pyautogui.press("enter")
    else:
        pyautogui.press("esc")
    pyautogui.moveTo(arrow_red_pos, duration=speed)
    pyautogui.press("esc")


def visib_check(antenna):
    if antenna == 0.6:
        return cross_ant_local
    if antenna == 1.2:
        return [cross_ant_local[0], cross_ant_local[1] + 100]
    if antenna == 0.3:
        return [cross_ant_local[0], cross_ant_local[1] + 200]


def cross_antennas(antenna, number):
    pyautogui.click()
    pyautogui.moveTo(visib_check(antenna[1]), duration=speed)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.click(prop_visib_pos)
    for elem in range(rotate_cross_antennas(set_cross_antennas_angle(antenna[0], tow_azimuth))[1]):
        pyautogui.typewrite(str(rotate_cross_antennas(set_cross_antennas_angle(antenna[0], tow_azimuth))[0]))
    pyautogui.moveTo(prop_below_vis_pos, duration=speed)
    pyautogui.click()
    pyautogui.typewrite(str(antenna[0]))
    pyautogui.press("enter")
    pyautogui.typewrite(str(number[2]))
    pyautogui.press("enter")
    pyautogui.click(visib_check(antenna[1]))
    if antenna == azimuth1[0] or antenna == azimuth1[1] or antenna == azimuth1[2]:
        move = [372, 165 + number[2] * 100]
    else:
        move = [1357, 165 + number[2] * 100]
    pyautogui.click(move)
    pyautogui.press("esc")


def set_cross_antennas_angle(azimuth, az_tow):
    if azimuth - az_tow > 0:
        return azimuth - az_tow
    else:
        return 360 + (azimuth - az_tow)


def rotate_cross_antennas(angle):
    angle = round(angle/10)
    if angle < 10:
        return [angle, 1]
    elif 10 <= angle < 20:
        return [1, angle - 8]
    elif 20 <= angle < 30:
        return [2, angle - 18]
    elif angle == 36:
        return [0, 0]
    else:
        return [3, angle - 28]


azimuth1, azimuth2 = sort_az_list()
towers_rotate(tow_azimuth, tow_check_E)
for enum, elem in enumerate(all_a):
    if elem in azimuth1:
        rotate(elem, elem, antennas_pos_w(elem, tow_azimuth, w1))
    else:
        rotate(elem, elem, antennas_pos_w(elem, tow_azimuth, w2))
for i in range(3):
    cross_antennas(azimuth1[i], azimuth1[i])
    cross_antennas(azimuth2[i], azimuth2[i])
pyautogui.typewrite("rea")
pyautogui.press("space")

if round(time.time() - begin_time,2) > 30:
    print("Damn, It took only", round(time.time() - begin_time,2), "sec. Maybe try type speed = 0. :)")
else:
    print("Wow, that was fast. It took only", round(time.time() - begin_time,2), "sec")
