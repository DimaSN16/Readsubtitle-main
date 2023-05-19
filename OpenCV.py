import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


filename = 'Image.png'
x = 1
last_time = time.time()

while(True):
    screen = np.array(ImageGrab.grab(bbox=(1218, 1009, 2039, 1078)))
    #print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imwrite(filename, screen)
    x = x + 1
    #print(x)

    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img)
    print(text)
    with open('Subtitle.txt', 'w') as text_file:
        text_file.write(text)
    cv2.destroyAllWindows()