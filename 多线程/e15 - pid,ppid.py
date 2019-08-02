import multiprocessing
import os

def getid():
    print('parent procss:' + str(os.getppid()))
    print('current process' + str(os.getpid()))

def get():
    getid()
    print('finish')

if __name__ == '__main__':
    getid()

    p = multiprocessing.Process(target=get)
    p.start()
    p.join()