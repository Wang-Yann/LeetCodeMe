#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 18:25:42
# @Last Modified : 2020-07-12 18:25:42
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 实现一个MyQueue类，该类用两个栈来实现一个队列。 示例： MyQueue queue = new MyQueue(); queue.push(1); 
# queue.push(2); queue.peek();  // 返回 1 queue.pop();   // 返回 1 queue.empty(); // 返
# 回 false 说明： 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty
#  操作是合法的。 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。 假设所有操作都是有效的 
# （例如，一个空的队列不会调用 pop 或者 peek 操作）。 Related Topics 栈 
#  👍 16 👎 0


"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE,BIG_RES







# leetcode submit region begin(Prohibit modification and deletion)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushs = []
        self.pops = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pushs.append(x)



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.pops)==0:
            for i in range(len(self.pushs)):
                self.pops.append(self.pushs.pop())
        return self.pops.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.pops)==0:
             while self.pushs:
                self.pops.append(self.pushs.pop())
        v = self.pops[-1]
        return v



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.pushs)==0 and len(self.pops)==0




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    queue =  MyQueue()

    queue.push(1)
    queue.push(2)
    assert queue.peek()==1 #  // 返回 1
    assert queue.pop()==1 #   // 返回 1
    assert not queue.empty()  # // 返回 false






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

