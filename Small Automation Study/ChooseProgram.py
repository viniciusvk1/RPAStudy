import pyautogui
import pyautogui as choose_option

choose = pyautogui.confirm("Click on the desired option", buttons = ["Excel", "Word", "Notepad"])

if choose == "Excel":
    print("Opened excel!")

    choose_option.hotkey("win", "r")
    choose_option.typewrite("excel")
    choose_option.press("enter")

    choose_option.sleep(1)

    choose_option.press("enter")
    choose_option.typewrite("Opened Excel!")

elif choose == "Word":
    print("Opened Word!")

    choose_option.hotkey("win", "r")
    choose_option.typewrite("winword")
    choose_option.press("enter")

    choose_option.sleep(1)

    choose_option.press("enter")
    choose_option.typewrite("Opened Word!")

elif choose == "Notepad":
    print("Opened Notepad!")

    choose_option.hotkey("win", "r")
    choose_option.typewrite("notepad")
    choose_option.press("enter")

    choose_option.sleep(0)

    choose_option.typewrite("Opened Notepad!")
