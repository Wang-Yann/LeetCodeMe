#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 19:36:06
# @Last Modified : 2020-04-25 19:36:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



"""
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
#  push(x) —— 将元素 x 推入栈中。
#  pop() —— 删除栈顶的元素。
#  top() —— 获取栈顶元素。
#  getMin() —— 检索栈中的最小元素。
#
#
#
#
#  示例:
#
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  pop、top 和 getMin 操作总是在 非空栈 上调用。
#
#  Related Topics 栈 设计
#  👍 606 👎 0

"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            last_min = self.stack[-1][1]
            self.stack.append((x, min(last_min, x)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            v, min_val = self.stack[-1]
            return v

    def getMin(self) -> int:
        if self.stack:
            last_min = self.stack[-1][1]
            return last_min


if __name__ == '__main__':
    obj = MinStack()
    obj.push(12)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
