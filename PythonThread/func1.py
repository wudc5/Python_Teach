# coding=utf-8
import threading


def thread_func(num):
    print num


if __name__ == "__main__":
    num = 10
    threads = list()
    for x in range(0, num):
        thread_name = "thread_%s" % x
        threads.append(threading.Thread(target=thread_func, name=thread_name, args=([10,20,30],)))
    # 启动所有线程
    for t in threads:
        t.start()
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join()
