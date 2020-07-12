#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 18:45:51
# @Last Modified : 2020-07-12 18:45:51
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定
# ）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如
# enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。 
# 
#  enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。 
# 
#  dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。 
# 
#  示例1: 
# 
#   输入：
# ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"
# ]
# [[], [[0, 0]], [[1, 0]], [], [], []]
#  输出：
# [null,null,null,[0,0],[-1,-1],[1,0]]
#  
# 
#  示例2: 
# 
#   输入：
# ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "
# dequeueAny"]
# [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
#  输出：
# [null,null,null,null,[2,1],[0,0],[1,0]]
#  
# 
#  说明: 
# 
#  
#  收纳所的最大容量为20000 
#  
#  Related Topics 设计 
#  👍 5 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class AnimalShelf:

    def __init__(self):
        self.arr = []

    def enqueue(self, animal: List[int]) -> None:
        self.arr.append(animal)

    def dequeueAny(self) -> List[int]:
        if self.arr:
            return self.arr.pop(0)
        return [-1, -1]

    def dequeueDog(self) -> List[int]:
        N = len(self.arr)
        i = 0
        ret = [-1, -1]
        while i < N:
            if self.arr[i][1] == 1:
                ret = self.arr[i]
                self.arr.pop(i)
                break
            i += 1
        return ret

    def dequeueCat(self) -> List[int]:
        N = len(self.arr)
        i = 0
        ret = [-1, -1]
        while i < N:
            if self.arr[i][1] == 0:
                ret = self.arr[i]
                self.arr.pop(i)
                break
            i += 1
        return ret


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    q = AnimalShelf()
    q.enqueue([0, 0])
    q.enqueue([1, 0])
    q.enqueue([2, 1])
    assert q.dequeueDog() == [2, 1]
    assert q.dequeueCat() == [0, 0]
    assert q.dequeueAny() == [1, 0]


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
