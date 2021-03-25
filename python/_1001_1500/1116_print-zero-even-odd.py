#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-04 20:03:12
# @Last Modified : 2020-07-04 20:03:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 假设有这么一个类： 
# 
#  class ZeroEvenOdd {
#   public ZeroEvenOdd(int n) { ... }      // 构造函数
#   public void zero(printNumber) { ... }  // 仅打印出 0
#   public void even(printNumber) { ... }  // 仅打印出 偶数
#   public void odd(printNumber) { ... }   // 仅打印出 奇数
# }
#  
# 
#  相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程： 
# 
#  
#  线程 A 将调用 zero()，它只输出 0 。 
#  线程 B 将调用 even()，它只输出偶数。 
#  线程 C 将调用 odd()，它只输出奇数。 
#  
# 
#  每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n
# 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出："0102"
# 说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
#  
# 
#  示例 2： 
# 
#  输入：n = 5
# 输出："0102030405"
#  
#  👍 54 👎 0

"""

import pytest


def printNumber(i):
    print(str(i))


# leetcode submit region begin(Prohibit modification and deletion)
import threading


class ZeroEvenOdd:

    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.gates = [threading.Semaphore(), threading.Semaphore(), threading.Semaphore()]
        self.gates[0].acquire()
        self.gates[1].acquire()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.gates[2].acquire()
            printNumber(0)
            self.ct += 1
            self.gates[self.ct % 2].release()

    def even(self, printNumber):
        for _ in range(self.n // 2):
            self.gates[0].acquire()
            printNumber(self.ct)
            self.gates[2].release()

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):
            self.gates[1].acquire()
            printNumber(self.ct)
            self.gates[2].release()


# leetcode submit region end(Prohibit modification and deletion)


class ZeroEvenOddLock:

    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.gates = [threading.Lock(), threading.Lock(), threading.Lock()]
        self.gates[0].acquire()
        self.gates[1].acquire()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.gates[2].acquire()
            printNumber(0)
            self.ct += 1
            self.gates[self.ct % 2].release()

    def even(self, printNumber):
        for _ in range(self.n // 2):
            self.gates[0].acquire()
            printNumber(self.ct)
            self.gates[2].release()

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):
            self.gates[1].acquire()
            printNumber(self.ct)
            self.gates[2].release()


class ZeroEvenOddBarrier:

    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.barriers = [threading.Barrier(2), threading.Barrier(2)]
        self.zero_lock = threading.Lock()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            self.ct += 1
            self.barriers[self.ct % 2].wait()

    def even(self, printNumber):
        for _ in range(self.n // 2):
            self.barriers[0].wait()
            printNumber(self.ct)
            self.zero_lock.release()

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):
            self.barriers[1].wait()
            printNumber(self.ct)
            self.zero_lock.release()


class ZeroEvenOddEvent:

    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.print = [threading.Event(), threading.Event(), threading.Event()]
        self.print[2].set()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.print[2].wait()
            self.print[2].clear()
            printNumber(0)
            self.ct += 1
            self.print[self.ct % 2].set()

    def even(self, printNumber):
        for _ in range(self.n // 2):
            self.print[0].wait()
            self.print[0].clear()
            printNumber(self.ct)
            self.print[2].set()

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):
            self.print[1].wait()
            self.print[1].clear()
            printNumber(self.ct)
            self.print[2].set()


class ZeroEvenOddCond:

    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.condition = threading.Condition()
        self.order = 2

    def zero(self, printNumber):
        for _ in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda:self.order == 2)
                printNumber(0)
                self.ct += 1
                self.order = self.ct % 2
                self.condition.notify(2)

    def even(self, printNumber):
        for _ in range(self.n // 2):
            with self.condition:
                self.condition.wait_for(lambda:self.order == 0)
                printNumber(self.ct)
                self.order = 2
                self.condition.notify(2)

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):
            with self.condition:
                self.condition.wait_for(lambda:self.order == 1)
                printNumber(self.ct)
                self.order = 2
                self.condition.notify(2)


@pytest.mark.parametrize("FooCls", [ZeroEvenOdd, ZeroEvenOddLock, ZeroEvenOddEvent, ZeroEvenOddCond])
@pytest.mark.parametrize("args,expected", [
    (2, "0102"),
    pytest.param(5, "0102030405"),
])
def test_solutions(capsys, args, expected, FooCls):
    foo = FooCls(args)
    with capsys.disabled():
        print("Foo Class: {}".format(foo.__class__.__name__))

    t1 = threading.Thread(target=foo.zero, args=(printNumber,))
    t2 = threading.Thread(target=foo.even, args=(printNumber,))
    t3 = threading.Thread(target=foo.odd, args=(printNumber,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    captured = capsys.readouterr()
    output = captured.out.replace("\n", "")
    assert output == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
