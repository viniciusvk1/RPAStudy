import pyautogui as mousePosition

mousePosition.sleep(1)
# print(mousePosition.position())

mousePosition.moveTo(x=15, y=1066)
mousePosition.click(x=15, y=1066)
mousePosition.sleep(1)

mousePosition.typewrite("Google Chrome")
mousePosition.sleep(1)
mousePosition.press("enter")

mousePosition.typewrite("Price of the dollar in real today ")

mousePosition.press("enter")