import pyautogui as pt
from time import sleep

pos1 = (100, 212)
pos2 = (1107, 246)
pos3 = (959, 683)
pos4 = (1149, 546)
pos5 = (1419, 160)

pt.moveTo(pos1)

i = 0
numOfLives = 0
while i < numOfLives:
    pt.click(pos1)
    sleep(.5)
    pt.click(pos2)
    sleep(.3)
    pt.click(pos3)
    sleep(.5)
    pt.click(pos4)
    sleep(.5)
    pt.click(pos5)
    sleep(1)
    i += 1



