import numpy as np
import cv2
import cython
import pyscreenshot as ImageGrab
import win32gui
from PIL import Image
from mss import mss

sct = mss()



maxDif = 5
playerColor = np.array([53, 43, 93])
block1Color = [79, 69, 93]
block2Color = [142, 132, 151]
playerLOC = [0,0,0,0]
LOC = {'top': 0, 'left': 0, 'width': 0, 'height': 0}
lastPos = 2

def getVid():
    hwd = win32gui.FindWindow(None, "SM-G950F")
    rect = win32gui.GetWindowRect(hwd)
    return {'top': rect[1]+50, 'left': rect[0], 'width': rect[2] - rect[0] , 'height': rect[3] - (rect[1]+50)}

def getPlayer(image):
    r, t = np.where((image[:,:,0] == 53) & (image[:,:,1] == 43) & (image[:,:,2] == 93))
    if len(t) < 1:
        return -1
    x = t[0]
    if x < 140:
        return 0
    if 140 < x < 200:
        return 1
    if 200 < x < 270:
        return 2
    if 270 < x < 330:
        return 3
    if x > 330:
        return 4

def updatePlayer():
    global lastPos
    img = np.array(sct.grab(LOC))
    image = np.array(img)
    output = image.copy()
    pos = getPlayer(image)
    if pos == -1:
        pos = lastPos
    lastPos = pos
    
    overlay = image.copy()
    if pos == 0:
        cv2.rectangle(overlay, (80,470), (140, 600), (0,0,255), 2)
    elif pos == 1:
        cv2.rectangle(overlay, (140,470), (200, 600), (0,0,255), 2)
    elif pos == 2:
        cv2.rectangle(overlay, (200,470), (270, 600), (0,0,255), 2)
    elif pos == 3:
        cv2.rectangle(overlay, (270,470), (330, 600), (0,0,255), 2)
    elif pos == 4:
        cv2.rectangle(overlay, (330,470), (390, 600), (0,0,255), 2)
    
    
    cv2.putText(overlay, str(pos), (230,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv2.addWeighted(overlay, 0.75, output, 0.25, 0, output)
    cv2.imshow("Player", output)
    cv2.waitKey(1)
    return

LOC = getVid()
print LOC
while True:
    updatePlayer()
    pass
    

