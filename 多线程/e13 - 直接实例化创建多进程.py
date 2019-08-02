import multiprocessing
import time

def clock(interval):
    for i in range(5):
        print('now is {}'.format(time.ctime()))
        time.sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(1,))
    p.start()
    p.join()