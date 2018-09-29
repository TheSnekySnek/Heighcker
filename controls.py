from subprocess import Popen, check_output
from time import sleep
from PIL import Image
from io import BytesIO
import threading

def saveImage():
    Popen(["adb", "exec-out", "screencap", "-p"])
    pass

def getImage():
    cm = check_output(["adb", "exec-out", "screencap", "-p"])
    image = Image.open(BytesIO(cm))
    r = image.getpixel((323, 1210))
    print(r)

    pass

def jump():
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "1"])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "53", str(2050)])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "54", str(3000)])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "48", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "49", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])

    sleep(0.02)
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    pass

def left():
    #Set coordinates
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "1"])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "53", str(850)])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "54", str(3525)])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "48", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "49", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])

    sleep(0.2)
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    pass

def right():
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "1"])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "53", str(3200)])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "54", str(3525)])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "48", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "49", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])

    sleep(0.2)
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    pass

def restart():
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "1"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "1"])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "53", str(2500)])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "54", str(3500)])

    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "48", "12"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "49", "12"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])

    sleep(0.2)
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "330", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "1", "325", "0"])
    Popen(["adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    pass

