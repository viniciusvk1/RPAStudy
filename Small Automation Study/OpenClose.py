import pyautogui as arqPosition

arqPosition.hotkey('win', 'r')

arqPosition.sleep(0)

arqPosition.typewrite('notepad')

arqPosition.press('enter')

arqPosition.typewrite('notepad was opened with a script using python RPA')

closeNotepad = arqPosition.getActiveWindow()
closeNotepad.close()

arqPosition.press('tab')

arqPosition.press('enter')