import threading

sum = 0
num = 100000

lock = threading.Lock()

def add():
    global sum, num

    for i in range(num):
        # 申请一把锁
        lock.acquire()
        sum += 1
        # 上了锁,就要解锁
        lock.release()
    print(sum)

def minus():
    global sum, num

    for i in range(num):
        lock.acquire()
        sum -= 1
        lock.release()
    print(sum)

if __name__ == '__main__':
    print('start')

    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=minus)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('end:{}'.format(sum))
