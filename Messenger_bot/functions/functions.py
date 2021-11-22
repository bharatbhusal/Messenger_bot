import pyperclip
import pyautogui as pt
from time import sleep
import os
from functions.variables import *


class Do:
    def move_to(*image):
        pt.moveTo(*image)

    def full_screen():
        position = pt.locateOnScreen(
            "../Images/undo.png", confidence=.60)
        if position != None:
            pt.press("f11")
        sleep(1)

    def reset_screen():
        # reset screen resolution
        Do.move_to(*Variables().reset_button)
        pt.keyDown("ctrl")
        pt.press("-")
        pt.keyUp("ctrl")
        pt.click()
        Do.move_to(*Variables().birthday_today)
        sleep(3)

    def search_name(name):
        Do.move_to(*Variables().search_box)
        pt.click()
        # search name
        pt.write(name)
        Do.move_to(*Variables().name_button)
        sleep(1)
        pt.click()
        sleep(1.5)

    def send_message(msg):
        # send message
        pt.click(Variables().message_bar)
        # pt.write(f"{msg}\n")
        sleep(0.1)

    def copy_text():
        sleep(1)
        pt.doubleClick()
        pt.keyDown("ctrl")
        pt.press("c")
        pt.keyUp("ctrl")
        is_birthday_today = pyperclip.paste()
        return is_birthday_today  


class Open:
    def browser(site):
        # open browser
        os.system(f"xdg-open {site}")
        sleep(1)

    def message_box():
        sleep(2)
        color = pt.pixel(1312, 517)
        color = color[2]
        if color == 255:
            Do.move_to(*Variables().message_button1)
        else:
            Do.move_to(*Variables().message_button2)
        # open message box
        pt.click()
        sleep(3)
