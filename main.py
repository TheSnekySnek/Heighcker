import threading
from controls import jump, right, left, restart, getImage
from msvcrt import getch


while True:
    c = ord(getch())
    if c == 224:
        key = ord(getch())
        print(key)
        if key == 72: #Down arrow
            t = threading.Thread(target=jump)
            t.start()
        elif key == 75: #Down arrow
            t = threading.Thread(target=left)
            t.start()
        elif key == 77: #Down arrow
            t = threading.Thread(target=right)
            t.start()
        elif key == 80: #Down arrow
            restart()
    elif c == 0:
        exit(0)