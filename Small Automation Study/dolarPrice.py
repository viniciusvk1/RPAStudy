import pyautogui as mousePosition

mousePosition.sleep(1)
# print(mousePosition.position())

mousePosition.moveTo(x=15, y=1066)
mousePosition.click(x=15, y=1066)
mousePosition.sleep(1)

mousePosition.typewrite("Google Chrome")
mousePosition.sleep(1)
mousePosition.press("enter")

mousePosition.sleep(1)
# print(mousePosition.position())

mousePosition.click(x=231, y=82)
mousePosition.typewrite("Price of the dollar in real today ")

mousePosition.sleep(0)
mousePosition.press("enter")