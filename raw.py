from time import sleep
import pyautogui as pt
import pyperclip


birthday_today = 650, 528
is_birthday_today0 = "Birthday is in 2 days\n"


def move_to(*image):
    pt.moveTo(*image)


def copy_text():
    sleep(1)
    pt.tripleClick()
    pt.keyDown("ctrl")
    pt.press("c")
    pt.keyUp("ctrl")
    is_birthday_today = pyperclip.paste()
    return is_birthday_today


def if_true():
    x, y = 0, 0
    pt.move(x, y-27)
    pt.click()
    print("message sent")
    sleep(2)
    pt.keyDown("altright")
    pt.press("left")
    pt.keyUp("altright")
    pt.move(x, y+27)
    # pt.click()


def if_false():
    posXY = pt.position()
    x = posXY[0] + 430
    y = posXY[1]
    sleep(1)
    pt.moveTo(x, y)
    copy_text()


def check_if_birthday_today():
    if copy_text() != is_birthday_today0:
        if_true()
    else:
        if_false()


sleep(2)
# move_to(birthday_today)
# for i in range(1):
#     copy_text()
#     check_if_birthday_today()


pt.moveTo(650, 652)