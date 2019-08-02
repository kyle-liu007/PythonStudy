import threading
import time

def func():
    print('start run func')

if __name__ == '__main__':
    t1 = threading.Timer(6, func)

    t1.start()

    for i in range(4):
        print('run {} times '.format(i))
        time.sleep(3)