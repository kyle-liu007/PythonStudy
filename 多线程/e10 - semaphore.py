import threading
import time

semphore = threading.Semaphore(3)

def func():
    if semphore.acquire():
        print(threading.currentThread().getName() + 'get semaphore')

        time.sleep(1)
        semphore.release()
        print(threading.currentThread().getName() + 'release semaphore')
for i in range(8):
    t = threading.Thread(target=func)
    t.start()