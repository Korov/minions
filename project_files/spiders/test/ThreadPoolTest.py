import threading
import time
from concurrent.futures import ThreadPoolExecutor

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
        return "thread id:%s, thread name:%s" % (self.thread_id, self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


# 创建一个最大容纳数量为5的线程池
with ThreadPoolExecutor(max_workers=5) as t:
    # 通过submit提交执行的函数到线程池中
    task1 = t.submit(ThreadDemo, 1, "Thread-1", 1)
    task2 = t.submit(ThreadDemo, 2, "Thread-2", 2)
    task3 = t.submit(ThreadDemo, 3, "Thread-3", 3)

    # 通过done来判断线程是否完成
    print(f"task1 running: {task1.done()}")
    print(f"task2 running: {task2.done()}")
    print(f"task3 running: {task3.done()}")

    time.sleep(2.5)
    print(f"task1 done: {task1.done()}")
    print(f"task2 done: {task2.done()}")
    print(f"task3 done: {task3.done()}")
    # 通过result来获取返回值
    print(f"task1 result: {task1.result()}")
    print(f"task2 result: {task2.result()}")
    print(f"task3 result: {task3.result()}")
