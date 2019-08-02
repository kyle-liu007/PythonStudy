import threading
import time
def s1():
    print('start s1')
    time.sleep(3.5)
    print('finish s1')

def s2():
    print('start s2')
    time.sleep(3)
    print('finish s2')

def main():
    print('start main')
    t1 = threading.Thread(target=s1)
    # 将t1设置为守护线程,注意,设置守护线程需要在开始线程之前
    t1.setDaemon(True)
    # 还可这样设置
    # ti.daemon = True
    t1.start()

    t2 = threading.Thread(target=s2)
    t2.start()

    print('finish main')

if __name__ == '__main__':
    main()