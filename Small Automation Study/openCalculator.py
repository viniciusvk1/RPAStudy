import pyautogui as mousePosition

mousePosition.sleep(4)
print(mousePosition.position())

mousePosition.moveTo(x=13, y=1064)
mousePosition.click(x=13, y=1064)

mousePosition.sleep(0)
# print(mousePosition.position())

mousePosition.typewrite("Calculator")
mousePosition.press("enter")