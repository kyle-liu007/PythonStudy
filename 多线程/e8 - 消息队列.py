import threading
import time
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 10:
                for i in range(10):
                    count += 1
                    msg = '产品{}'.format(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 5:
                for i in range(3):
                    msg = self.name + '消费了' + queue.get()
                    print(msg)
            time.sleep(0.5)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(5):
        queue.put('初始产品' + str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()
