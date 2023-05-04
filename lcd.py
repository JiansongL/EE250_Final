import time
from grove_rgb_lcd import *

setRGB(0, 255, 0)       #set RGB color for LCD
file = open("./speech.txt", "r")        # read speech.txt from the current folder
for text in file:
        time.sleep(3)
        setText(text)   # print each line in the speech.txt
file.close()
