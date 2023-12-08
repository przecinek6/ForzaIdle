from KeyboardEvents import *


def findimage(image_name):
    error = 0
    filename = f'img/{image_name}.png'

    while True:
        try:
            x, y = pyag.locateCenterOnScreen(filename, confidence=0.8)
            break

        except pyag.ImageNotFoundException:
            time.sleep(1)
            error += 1
            if error > 60:
                print(f'Unexpected  error at {image_name} segment...')
                exit(image_name)

    pyag.moveTo(x, y)  # Setting cursor on current coordinates

    if image_name != 4:
        time.sleep(0.2)  # Time before next click
        pyag.mouseDown()  # Mouse click down
        pyag.mouseUp()  # Mouse click up

    time.sleep(0.2)  # Time before next click
    pyag.mouseDown()  # Mouse click down
    pyag.mouseUp()  # Mouse click up



def findimage_end():
    error = 0
    while True:
        try:
            pyag.locateOnScreen('img/end.png', confidence=0.8)
            break

        except pyag.ImageNotFoundException:
            press_enter()
            time.sleep(1)
            error += 1

            if error > 60:
                print(f'Unexpected  error at last segment...')
                exit('last')