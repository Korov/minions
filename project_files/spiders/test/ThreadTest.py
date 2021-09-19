import threading
import time

exitFlag = 0

class ThreadDemo(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)

    def result(self):
        threading.Thread.join(self)
        return "thread id:%s, thread name:%s" % (self.thread_id, self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = ThreadDemo(1, "Thread-1", 1)
thread2 = ThreadDemo(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
print("thread1 result:%s" % (thread1.result()))
print("thread2 result:%s" % (thread2.result()))
print("退出主线程")
