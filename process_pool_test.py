import multiprocessing
import time
import os
import random


def test1(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print("%s执行完成，耗时%.2f" % (msg, t_stop - t_start))


if __name__ == "__main__":

    po = multiprocessing.Pool(3)
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(test1, (i,))

    print("-----start-----")

    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后

    print("-----end-----")