import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    # 创建Thread子类时,必须重写run函数,run函数内才是该子类的实例线程真正执行的操作
    def run(self):
        time.sleep(2)
        print('重写了run')

t = MyThread()
t.start()
t.join()

print('over')