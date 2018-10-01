import numpy as np
import cv2
import cython
import pyscreenshot as ImageGrab
import win32gui
from PIL import Image
from mss import mss

sct = mss()

tbl1 = cv2.imread('template1.png',0)

maxDif = 5
playerColor = np.array([53, 43, 93])
blockColors = [
    [155, 135, 145],
    [133, 110, 123],
    [100, 78, 89],
    [86, 64, 75]
]
playerLOC = [0,0,0,0]
LOC = {'top': 0, 'left': 0, 'width': 0, 'height': 0}
lastPos = 2

def getVid():
    hwd = win32gui.FindWindow(None, "SM-G950F")
    rect = win32gui.GetWindowRect(hwd)
    return {'top': rect[1]+50, 'left': rect[0], 'width': rect[2] - rect[0] , 'height': rect[3] - (rect[1]+50)}

def getObj(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    w, h = tbl1.shape[::-1]
    res = cv2.matchTemplate(img_gray,tbl1,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where(res >= threshold)
    return loc, w, h

def isBlock(pixels):
    for x in range(len(blockColors)):
        if blockColors[x][0]-maxDif < pixels[0] < blockColors[x][0]+maxDif and blockColors[x][1]-maxDif < pixels[1] < blockColors[x][1]+maxDif and blockColors[x][2]-maxDif < pixels[2] < blockColors[x][2]+maxDif:
            return True
        return False
    

def getObjects(image):
    objs = [False, False, False, False, False]
    for x in range(480):
        if isBlock(image[110, x]):
            if x < 140:
                objs[0] = True
            if 140 < x < 200:
                objs[1] = True
            if 200 < x < 270:
                objs[2] = True
            if 270 < x < 330:
                objs[3] = True
            if x > 330:
                objs[4] = True
    return objs

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
        cv2.putText(overlay, "PLAYER", (80, 620), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (80,470), (140, 600), (0,0,255), 2)
    elif pos == 1:
        cv2.putText(overlay, "PLAYER", (140, 620), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (140,470), (200, 600), (0,0,255), 2)
    elif pos == 2:
        cv2.putText(overlay, "PLAYER", (200, 620), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (200,470), (270, 600), (0,0,255), 2)
    elif pos == 3:
        cv2.putText(overlay, "PLAYER", (270, 620), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (270,470), (330, 600), (0,0,255), 2)
    elif pos == 4:
        cv2.putText(overlay, "PLAYER", (330, 620), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (330,470), (390, 600), (0,0,255), 2)

    objs = getObjects(image)
    #print objs
    if objs[0]:
        cv2.putText(overlay, "BLOCK", (80, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (80,110), (140, 200), (0,0,255), 2)
    if objs[1]:
        cv2.putText(overlay, "BLOCK", (140, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (140,110), (200, 200), (0,0,255), 2)
    if objs[2]:
        cv2.putText(overlay, "BLOCK", (200, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (200,110), (270, 200), (0,0,255), 2)
    if objs[3]:
        cv2.putText(overlay, "BLOCK", (270, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (270,110), (330, 200), (0,0,255), 2)
    if objs[4]:
        cv2.putText(overlay, "BLOCK", (330, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 3)
        cv2.rectangle(overlay, (330,110), (390, 200), (0,0,255), 2)

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
    

