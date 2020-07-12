#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 15:07:35
# @Last Modified : 2020-07-12 15:07:35
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 三合一。描述如何只用一个数组来实现三个栈。 
# 
#  你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。s
# tackNum表示栈下标，value表示压入的值。 
# 
#  构造函数会传入一个stackSize参数，代表每个栈的大小。 
# 
#  示例1: 
# 
#   输入：
# ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
# [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
#  输出：
# [null, null, null, 1, -1, -1, true]
# 说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
#  
# 
#  示例2: 
# 
#   输入：
# ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
# [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
#  输出：
# [null, null, null, null, 2, 1, -1, -1]
#  
#  Related Topics 设计 
#  👍 10 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class TripleInOne:

    def __init__(self, stackSize: int):
        self.numstacks = 3
        self.array = [0] * (stackSize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.__IsFull(stackNum):
            return
        self.sizes[stackNum] += 1
        self.array[self.__IndexOfTop(stackNum)] = value

    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        value = self.array[self.__IndexOfTop(stackNum)]
        self.array[self.__IndexOfTop(stackNum)] = 0
        self.sizes[stackNum] -= 1
        return value

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            return -1
        return self.array[self.__IndexOfTop(stackNum)]

    def isEmpty(self, stackNum: int) -> bool:
        return self.sizes[stackNum] == 0

    def __IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def __IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    sol = TripleInOne(2)
    sol.push(0, 1)
    sol.push(0, 2)
    sol.push(0, 3)
    assert sol.pop(0) == 2
    assert sol.pop(0) == 1
    assert sol.pop(0) == -1
    assert sol.peek(0) == -1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
