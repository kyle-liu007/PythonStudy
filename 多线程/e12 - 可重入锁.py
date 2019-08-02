import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if l.acquire():
            num += 1
            msg = self.name + ' set num to ' + str(num)
            print(msg)
            l.acquire()
            l.release()
            l.release()

num = 0

l = threading.RLock()

if __name__ == '__main__':
    t = MyThread()
    t.start()
