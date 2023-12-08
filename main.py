from FindImage import *
from KeyboardEvents import *


loop = 1  # variable means how many times loop in program was finished
time.sleep(8)  # waiting time before program runs

while True:
    pyag.moveTo(10, 10) # Basic cursor position
    print("Loop = ", loop)
    press_esc()
    findimage(1)
    findimage(2)
    findimage(3)
    findimage(4)
    findimage(5)
    findimage(6)
    findimage(7)
    findimage(8)
    time.sleep(3) # animation time
    hold_space(43)
    findimage_end()

    loop = loop + 1