#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 11:21:33
# @Last Modified : 2020-07-27 11:21:33
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。 
# 
#  示例: 
# 
#  输入:
# v1 = [1,2]
# v2 = [3,4,5,6] 
# 
# 输出: [1,3,2,4,5,6]
# 
# 解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
#      next 函数返回值的次序应依次为: [1,3,2,4,5,6]。 
# 
#  拓展：假如给你 k 个一维向量呢？你的代码在这种情况下的扩展性又会如何呢? 
# 
#  拓展声明： 
#  “锯齿” 顺序对于 k > 2 的情况定义可能会有些歧义。所以，假如你觉得 “锯齿” 这个表述不妥，也可以认为这是一种 “循环”。例如： 
# 
#  输入:
# [1,2,3]
# [4,5,6,7]
# [8,9]
# 
# 输出: [1,4,8,2,5,9,3,6,7].
#  
#  Related Topics 设计 
#  👍 16 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.dq = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self) -> int:
        l, iterator = self.dq.popleft()
        if l > 1:
            self.dq.append((l - 1, iterator))
        return next(iterator)

    def hasNext(self) -> bool:
        return bool(self.dq)

    # Your ZigzagIterator object will be instantiated and called as such:


# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    obj = ZigzagIterator(v1=[1, 2], v2=[3, 4, 5, 6])
    expected = [1, 3, 2, 4, 5, 6]
    iter_e = iter(expected)
    while obj.hasNext():
        assert next(iter_e) == obj.next()


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
