#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Pipe
import os, time, random


def write(conn):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        conn.send('This is a message!')
        time.sleep(random.random())


def read(conn):
    print('Process to write: %s' % os.getpid())
    while True:  # 因为不知道什么时候结束，所以这里用while True
        value = conn.recv()
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    parent_conn, child_conn = Pipe()
    pw = Process(target=write, args=(child_conn,))  # 一个方向用来写
    pr = Process(target=read, args=(parent_conn,))  # 管道的另外个方向用来接受
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()  # 强制结束
