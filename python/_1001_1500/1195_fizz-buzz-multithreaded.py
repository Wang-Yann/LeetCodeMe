#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-04 21:49:18
# @Last Modified : 2020-07-04 21:49:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是： 
# 
#  
#  如果这个数字可以被 3 整除，输出 "fizz"。 
#  如果这个数字可以被 5 整除，输出 "buzz"。 
#  如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。 
#  
# 
#  例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14
# , fizzbuzz。 
# 
#  假设有这么一个类： 
# 
#  class FizzBuzz {
#   public FizzBuzz(int n) { ... }               // constructor
#   public void fizz(printFizz) { ... }          // only output "fizz"
#   public void buzz(printBuzz) { ... }          // only output "buzz"
#   public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
#   public void number(printNumber) { ... }      // only output the numbers
# } 
# 
#  请你实现一个有四个线程的多线程版 FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用： 
# 
#  
#  线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。 
#  线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。 
#  线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。 
#  线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。 
#  
#  👍 23 👎 0

"""

import pytest


def printFizz():
    print("fizz")


def printBuzz():
    print("buzz")


def printFizzBuzz():
    print("fizzbuzz")


def printNumber(i):
    print(str(i))


# leetcode submit region begin(Prohibit modification and deletion)
from threading import Semaphore, Thread


class FizzBuzz:

    def __init__(self, n: int):
        self.n = n
        self.sem = Semaphore()  # default is 1
        self.sem3 = Semaphore(0)
        self.sem5 = Semaphore(0)
        self.sem15 = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        i = 3
        while i <= self.n:
            self.sem3.acquire()
            printFizz()
            i += 3
            if i % 5 == 0:
                i += 3
            self.sem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        i = 5
        while i <= self.n:
            self.sem5.acquire()
            printBuzz()
            i += 5
            if i % 3 == 0:
                i += 5
            self.sem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n + 1, 15):
            self.sem15.acquire()
            printFizzBuzz()
            self.sem.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem.acquire()
            if i % 15 == 0:
                self.sem15.release()
            elif i % 5 == 0:
                self.sem5.release()
            elif i % 3 == 0:
                self.sem3.release()
            else:
                printNumber(i)
                self.sem.release()


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("FizzBuzzCls", [FizzBuzz])
@pytest.mark.parametrize("args,expected", [
    (15, "12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz"),
])
def test_solutions(capsys, args, expected, FizzBuzzCls):
    foo = FizzBuzzCls(args)
    with capsys.disabled():
        print("FizzBuzzCls Class: {}".format(foo.__class__.__name__))
    t1 = Thread(target=foo.fizz, args=(printFizz,))
    t2 = Thread(target=foo.buzz, args=(printBuzz,))
    t3 = Thread(target=foo.fizzbuzz, args=(printFizzBuzz,))
    t4 = Thread(target=foo.number, args=(printNumber,))
    threads = [t1, t2, t3, t4]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    captured = capsys.readouterr()
    output = captured.out.replace("\n", "")
    assert output in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
