from image_operations import *


running = False


def forza_instructions():
    global running
    running = True

    time.sleep(1)  # waiting time before program runs
    while running:
        press_esc()
        findimage(1)
        findimage(2)
        findimage(3)
        findimage(4)
        findimage(5)
        findimage(6)
        findimage(7)
        findimage(8)
        time.sleep(3)  # animation time
        hold_space(43)
        findimage_end()
