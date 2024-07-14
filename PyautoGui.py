import pyautogui
import time

## give the python  file some time before continuining

time.sleep(3)

## mouse functions

print(pyautogui.size())   # Prints the resolution to your screen
#prints the currrent position of the mouse
print(pyautogui.position())

#Moves teh mouse over time (3 seconds /add the time which can makes you comfortable)
pyautogui.moveTo(100,100,3)

#move the mouse to relative its current position

pyautogui.moveRel(100,100,3)

 #mouse click functions
pyautogui.click(500,500,3,3,button="left")
pyautogui.tripleClick()
pyautogui.doubleClick()
pyautogui.leftClick()
pyautogui.rightClick()

## scrolls up 500
pyautogui.scroll(500)
#scrolls down
pyautogui.scroll(-500)

##mouse up and Down
pyautogui.mouseUp(100,100,button="left")
pyautogui.mouseDown(100,100,button="right")


## trial for mouse up and Down

pyautogui.mouseDown(300,400,button="left")
pyautogui.moveTo(800,400,3)
pyautogui.mouseUp()
pyautogui.moveTo(1000,400,3)

##spiral drawing using the pyautogui

time.sleep(1)
distance = 300
while distance > 0:
    pyautogui.dragRel(distance,0,1,button="left")
    pyautogui = distance -20
    pyautogui.dragRel(0,distance,1,button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    pyautogui = distance -20
    pyautogui.dragRel(0, -distance, 1, button="left")
time.sleep(2)



