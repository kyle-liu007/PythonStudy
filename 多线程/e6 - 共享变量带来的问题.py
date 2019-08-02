import threading

a = 1
num = 100000

def add():
    global a, num
    for i in range(num):
        a += 1

def minus():
    global a, num
    for i in range(num):
        a -= 1

if __name__ == '__main__':
    print('start')

    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=minus)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('end:{}'.format(a))
