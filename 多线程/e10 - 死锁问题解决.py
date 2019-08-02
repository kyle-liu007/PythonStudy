import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def fun_1():
    print('fun_1 start')
    print('fun_1 ask for lock_1')
    lock_1.acquire(timeout = 2)
    time.sleep(2)
    print('fun_1 wait for lock_2')
    rst = lock_2.acquire(timeout = 2)
    if rst == True:
        print('fun_1 get lock_2')
        lock_2.release()
    else :
        print('fun_1 dosen\'t get lock_2')
    lock_1.release()

def fun_2():
    print('fun_2 start')
    print('fun_2 ask for lock_2')
    lock_2.acquire(timeout = 2)
    time.sleep(2)
    print('fun_2 wait for lock_1')
    rst = lock_1.acquire(timeout = 4)
    if rst == True:
        print('fun_2 get lock_1')
        lock_1.release()
    else:
        print('fun_2 doesn\'t get lock_1')
    lock_2.release()

if __name__ == '__main__':
    print('the main process starts')

    t1 = threading.Thread(target=fun_1)
    t2 = threading.Thread(target=fun_2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('the main process ends')