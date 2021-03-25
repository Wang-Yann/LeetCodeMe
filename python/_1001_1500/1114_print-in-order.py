#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-04 10:43:33
# @Last Modified : 2020-07-04 10:43:33
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们提供了一个类： 
# 
#  
# public class Foo {
#   public void one() { print("one"); }
#   public void two() { print("two"); }
#   public void three() { print("three"); }
# }
#  
# 
#  三个不同的线程将会共用一个 Foo 实例。 
# 
#  
#  线程 A 将会调用 one() 方法 
#  线程 B 将会调用 two() 方法 
#  线程 C 将会调用 three() 方法 
#  
# 
#  请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3]
# 输出: "onetwothree"
# 解释: 
# 有三个线程会被异步启动。
# 输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
# 正确的输出是 "onetwothree"。
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,3,2]
# 输出: "onetwothree"
# 解释: 
# 输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
# 正确的输出是 "onetwothree"。 
# 
#  
# 
#  注意: 
# 
#  尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。 
# 
#  你看到的输入格式主要是为了确保测试的全面性。 
#  👍 143 👎 0

"""
import queue
import threading
from typing import Callable

import pytest


def printFirst():
    print("one")


def printSecond():
    print("two")


def printThird():
    print("three")


# leetcode submit region begin(Prohibit modification and deletion)
class Foo:

    def __init__(self):
        self.c = threading.Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.__task(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.__task(1, printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.__task(2, printThird)

    def __task(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda:val == self.t)
            func()
            self.t += 1
            self.c.notify_all()


# leetcode submit region end(Prohibit modification and deletion)


class FooLock:

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock1:
            printSecond()
            self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock2:
            printThird()


class FooEvent:

    def __init__(self):
        self.done1 = threading.Event()
        self.done2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.done1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.done1.wait()
        printSecond()
        self.done2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.done2.wait()
        printThird()


class FooSemaphore:

    def __init__(self):
        self.gate1 = threading.Semaphore(0)
        self.gate2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.gate1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.gate1:
            printSecond()
            self.gate2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.gate2:
            printThird()


class FooBarrier:

    def __init__(self):
        self.barrier1 = threading.Barrier(2)
        self.barrier2 = threading.Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.barrier1.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.barrier1.wait()
        printSecond()
        self.barrier2.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.barrier2.wait()
        printThird()


class FooQueue:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()


@pytest.mark.parametrize("FooCls", [Foo, FooLock, FooEvent, FooSemaphore, FooBarrier,FooQueue])
@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3], "one\ntwo\nthree\n"),
    pytest.param([1, 3, 2], "one\ntwo\nthree\n"),
])
def test_solutions(capsys, args, expected, FooCls):
    foo = FooCls()
    with capsys.disabled():
        print("Foo Class: {}".format(foo.__class__.__name__))
    t3 = threading.Thread(target=foo.third, args=(printThird,))
    t1 = threading.Thread(target=foo.first, args=(printFirst,))
    t2 = threading.Thread(target=foo.second, args=(printSecond,))
    for i in args:
        if i == 1:
            t1.start()
        elif i == 2:
            t2.start()
        elif i == 3:
            t3.start()
    t1.join()
    t2.join()
    t3.join()

    captured = capsys.readouterr()
    assert captured.out == expected


# or use "capfd" for fd-level
# JUst Test For pytest sys out
#
# def test_myoutput1():
#     print("hello")
#     print("next")
#     assert 1 + 1 == 2
#
#
# def test_myoutput(capsys):
#     print("hello")
#     sys.stderr.write("world\n")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
#     assert captured.err == "world\n"
#     print("next")
#     captured = capsys.readouterr()
#     assert captured.out == "next\n"


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
