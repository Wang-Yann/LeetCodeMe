#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-04 20:43:06
# @Last Modified : 2020-07-04 20:43:06
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 现在有两种线程，氧 oxygen 和氢 hydrogen，你的目标是组织这两种线程来产生水分子。 
# 
#  存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。 
# 
#  氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。 
# 
#  这些线程应该三三成组突破屏障并能立即组合产生一个水分子。 
# 
#  你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。 
# 
#  换句话说: 
# 
#  
#  如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。 
#  如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。 
#  
# 
#  书写满足这些限制条件的氢、氧线程同步代码。 
# 
#  
# 
#  示例 1: 
# 
#  输入: "HOH"
# 输出: "HHO"
# 解释: "HOH" 和 "OHH" 依然都是有效解。
#  
# 
#  示例 2: 
# 
#  输入: "OOHHHH"
# 输出: "HHOHHO"
# 解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OH
# HOHH" 依然都是有效解。
#  
# 
#  
# 
#  提示： 
# 
#  
#  输入字符串的总长将会是 3n, 1 ≤ n ≤ 50； 
#  输入字符串中的 “H” 总数将会是 2n 。 
#  输入字符串中的 “O” 总数将会是 n 。 
#  
#  👍 60 👎 0

"""
import time

import pytest


def releaseHydrogen():
    print("H")


def releaseOxygen():
    print("O")


# leetcode submit region begin(Prohibit modification and deletion)
from threading import Barrier, Semaphore, Thread


class H2O:

    def __init__(self):
        self.barrier = Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o.release()


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("H2OCls", [H2O])
@pytest.mark.parametrize("args,expected", [
    ("HOH", ["HHO", "HOH", "OHH"]),
    pytest.param("OOHHHH", ["HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH", "OHHOHH"]),
])
def test_solutions(capsys, args, expected, H2OCls):
    foo = H2OCls()
    with capsys.disabled():
        print("Foo Class: {}".format(foo.__class__.__name__))
    threads=[]
    for char in args:
        if char == "H":
            t1 = Thread(target=foo.hydrogen, args=(releaseHydrogen,))
            t1.start()
            threads.append(t1)
        else:
            t2 = Thread(target=foo.oxygen, args=(releaseOxygen,))
            # daemonized thread - 'ignores' lifetime of other threads;
            # terminates when main-programs exits; No Need join
            # t2.setDaemon(True)
            t2.start()
            threads.append(t2)

    for t in threads:
        t.join()
    captured = capsys.readouterr()
    output = captured.out.replace("\n", "")
    assert output in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
