import pyautogui

text = "Hello hello hello hello hello hello hello Hello hello hello hello hello hello hello Hello hello hello hello hello hello hello"
for a in text.split():
	pyautogui.write(a)
	pyautogui.press("enter")
	
