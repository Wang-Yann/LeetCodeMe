#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-04 19:31:08
# @Last Modified : 2020-07-04 19:31:08
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们提供一个类： 
# 
#  
# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }
# 
#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
#  
# 
#  两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。 
# 
#  请设计修改程序，以确保 "foobar" 被输出 n 次。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 1
# 输出: "foobar"
# 解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 2
# 输出: "foobarfoobar"
# 解释: "foobar" 将被输出两次。
#  
#  👍 63 👎 0

"""
import threading

import pytest


def printFoo():
    print("foo")


def printBar():
    print("bar")


# leetcode submit region begin(Prohibit modification and deletion)
class FooBar:

    def __init__(self, n):
        self.n = n
        self.barrier = threading.Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barrier.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.barrier.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()


# leetcode submit region end(Prohibit modification and deletion)


class FooBarSem:

    def __init__(self, n):
        self.n = n
        self.foo_gate = threading.Semaphore(1)
        self.bar_gate = threading.Semaphore(0)

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_gate.acquire()
            printFoo()
            self.bar_gate.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.bar_gate.acquire()
            printBar()
            self.foo_gate.release()


class FooBarLock:

    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo):
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar):
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


class FooBarEvent:

    def __init__(self, n):
        self.n = n
        self.foo_printed = threading.Event()
        self.bar_printed = threading.Event()
        self.bar_printed.set()

    def foo(self, printFoo):
        for i in range(self.n):
            self.bar_printed.wait()
            self.bar_printed.clear()
            printFoo()
            self.foo_printed.set()

    def bar(self, printBar):
        for i in range(self.n):
            self.foo_printed.wait()
            self.foo_printed.clear()
            printBar()
            self.bar_printed.set()


class FooBarCond:

    def __init__(self, n):
        self.n = n
        self.foo_counter = 0
        self.bar_counter = 0
        self.condition = threading.Condition()

    def foo(self, printFoo):
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda:self.foo_counter == self.bar_counter)
                printFoo()
                self.foo_counter += 1
                self.condition.notify(1)

    def bar(self, printBar):
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda:self.foo_counter > self.bar_counter)
                printBar()
                self.bar_counter += 1
                self.condition.notify(1)


@pytest.mark.parametrize("FooCls", [FooBar, FooBarSem, FooBarLock, FooBarEvent, FooBarCond])
@pytest.mark.parametrize("args,expected", [
    (1, "foobar"),
    pytest.param(2, "foobarfoobar"),
])
def test_solutions(capsys, args, expected, FooCls):
    foo = FooCls(args)
    with capsys.disabled():
        print("Foo Class: {}".format(foo.__class__.__name__))

    t1 = threading.Thread(target=foo.foo, args=(printFoo,))
    t2 = threading.Thread(target=foo.bar, args=(printBar,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    captured = capsys.readouterr()
    # print(captured.output)
    output = captured.out.replace("\n", "")
    assert output == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
