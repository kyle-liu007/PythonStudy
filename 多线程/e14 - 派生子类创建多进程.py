import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        for i in range(5):
            print('start this process')
            time.sleep(1)

m = MyProcess()

if __name__ == '__main__':
    m.start()
    m.join()