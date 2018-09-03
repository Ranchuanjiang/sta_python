# 多个消费者 设置哨兵
import multiprocessing
from time import ctime, sleep


def consumer(input_q):
    print("消费者进程启动", ctime())
    while True:

        item = input_q.get()
        if item is None:
            break
        print("拿出来从", item, ctime())
    print("结束消费者进程")


def producer(sequence, output_q):
    print("生产者进程启动", ctime())
    for item in sequence:
        sleep(1)
        output_q.put(item)
        print("put", item, "into q")
    print("输出完毕", ctime())


if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    cons_q = multiprocessing.Process(target=consumer, args=(q,))
    cons_q1 = multiprocessing.Process(target=consumer, args=(q,))
    cons_q.daemon = True

    cons_q1.daemon = True
    cons_q1.start()
    cons_q.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    q.put(None)
    q.put(None)
    cons_q.join()
    cons_q1.join