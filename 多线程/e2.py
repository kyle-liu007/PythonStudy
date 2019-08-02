import threading
import time
def s1():
    print('start s1')
    time.sleep(3.5)
    print('finish s1')

def s2():
    print('start s2')
    time.sleep(3.5)
    print('finish s2')

def main():
    print('start main')
    t1 = threading.Thread(target=s1)
    t1.start()

    t2 = threading.Thread(target=s2)
    t2.start()

    t1.join()
    t2.join()

    print('finish main')

if __name__ == '__main__':
    main()