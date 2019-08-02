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
    threading._start_new_thread(s1, ())
    threading._start_new_thread(s2, ())
    print('fininsh the main')

if __name__ == '__main__':
    main()
    time.sleep(4)