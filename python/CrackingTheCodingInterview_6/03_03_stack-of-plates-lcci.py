#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 18:19:23
# @Last Modified : 2020-07-12 18:19:23
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行
# 为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与
# 普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行p
# op操作。 
# 
#  当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1. 
# 
#  示例1: 
# 
#   输入：
# ["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
# [[1], [1], [2], [1], [], []]
#  输出：
# [null, null, null, 2, 1, -1]
#  
# 
#  示例2: 
# 
#   输入：
# ["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
# [[2], [1], [2], [3], [0], [0], [0]]
#  输出：
# [null, null, null, null, 2, 1, 3]
#  
#  Related Topics 设计 
#  👍 5 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.arr = []

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if not self.arr or len(self.arr[-1]) >= self.cap:
            self.arr.append([val])
        else:
            self.arr[-1].append(val)

    def pop(self) -> int:
        if self.arr and self.arr[-1]:
            val = self.arr[-1].pop()
            if not self.arr[-1]:
                self.arr.pop()
            return val

        return -1

    def popAt(self, index: int) -> int:
        if len(self.arr) - 1 >= index:
            val = self.arr[index].pop()
            if not self.arr[index]:
                self.arr.pop(index)
            return val
        return -1


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    s = StackOfPlates(2)
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.popAt(0) == 2
    assert s.popAt(0) == 1
    assert s.popAt(0) == 3


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
