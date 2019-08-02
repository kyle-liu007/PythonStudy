import threading
import time

def s1():
    print('start s1')
    time.sleep(3.5)
    print('finish s1')

def s2():
    print('start s2')
    time.sleep(1)
    print('finish s2')

def main():
    print('start main')
    t1 = threading.Thread(target=s1, args=())
    t1.setName('T1')
    t1.start()

    t2 = threading.Thread(target=s2, args=())
    t2.setName('T2')
    t2.start()

    for i in threading.enumerate():
        print('当前正在运行的子线程：{0}'.format(i.getName()))
    print(threading.active_count())
    print('finish main')

if __name__ == '__main__':
    main()