#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 11:20:14
# @Last Modified : 2020-07-31 11:20:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个最大栈，支持 push、pop、top、peekMax 和 popMax 操作。 
# 
#  
# 
#  
#  push(x) -- 将元素 x 压入栈中。 
#  pop() -- 移除栈顶元素并返回这个值。 
#  top() -- 返回栈顶元素。 
#  peekMax() -- 返回栈中最大元素。 
#  popMax() -- 返回栈中最大的元素，并将其删除。如果有多个最大元素，只要删除最靠近栈顶的那个。 
#  
# 
#  
# 
#  样例 1: 
# 
#  MaxStack stack = new MaxStack();
# stack.push(5); 
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
#  
# 
#  
# 
#  注释: 
# 
#  
#  -1e7 <= x <= 1e7 
#  操作次数不会超过 10000。 
#  当栈为空的时候不会出现后四个操作。 
#  
# 
#  
#  Related Topics 设计 
#  👍 34 👎 0

"""
import math

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        m = max(x, self.stack[-1][1] if self.stack else -math.inf)
        self.stack.append((x, m))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.stack.pop()[0])
        self.stack.pop()
        for ele in reversed(b):
            self.push(ele)
        return m

    # Your MaxStack object will be instantiated and called as such:


# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(5)
    assert stack.top() == 5
    assert stack.popMax() == 5
    assert stack.top() == 1
    assert stack.peekMax() == 5
    assert stack.pop() == 1
    assert stack.top() == 5
    stack.push(1)
    stack.push(3)
    stack.push(4)
    stack.push(7)
    assert stack.popMax() == 7
    assert stack.popMax() == 5


#


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
