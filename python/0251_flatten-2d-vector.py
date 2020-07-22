#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 21:52:33
# @Last Modified : 2020-07-22 21:52:33
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 next 和 hasNext 两种操作。、 
# 
#  示例： 
# 
#  Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
# 
# iterator.next(); // 返回 1
# iterator.next(); // 返回 2
# iterator.next(); // 返回 3
# iterator.hasNext(); // 返回 true
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 4
# iterator.hasNext(); // 返回 false
#  
# 
#  
# 
#  注意： 
# 
#  
#  请记得 重置 在 Vector2D 中声明的类变量（静态变量），因为类变量会 在多个测试用例中保持不变，影响判题准确。请 查阅 这里。 
#  你可以假定 next() 的调用总是合法的，即当 next() 被调用时，二维向量总是存在至少一个后续元素。 
#  
# 
#  
# 
#  进阶： 
# 
#  尝试在代码中仅使用 C++ 提供的迭代器 或 Java 提供的迭代器。 
#  Related Topics 设计 
#  👍 20 👎 0

"""



import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE,BIG_RES







# leetcode submit region begin(Prohibit modification and deletion)
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.data = []
        for l in v:
            self.data.extend(l)
        self.pos = -1

    def next(self) -> int:
        self.pos += 1
        return self.data[self.pos]

    def hasNext(self) -> bool:
        return self.pos < len(self.data) - 1





# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# leetcode submit region end(Prohibit modification and deletion)



def test_solution251():
    iterator = Vector2D([[1, 2], [3], [4]])

    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.hasNext()
    assert iterator.hasNext()
    assert iterator.next() == 4
    assert not iterator.hasNext()



if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

