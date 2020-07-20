#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 23:17:56
# @Last Modified : 2020-05-06 23:17:56
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
#
#
#
#  示例:
#
#  MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  各函数的调用总次数不超过 20000 次
#
#
#
#
#  注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
#  Related Topics 栈 设计
#  👍 28 👎 0


import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]


    def push(self, x: int) -> None:
        if self.stack:
            current_min=min(x,self.stack[-1][0])
            self.stack.append((current_min,x))
        else:
            self.stack.append((x,x))




    def pop(self) -> None:
        return self.stack.pop()[1]


    def top(self) -> int:
        return self.stack[-1][1]


    def min(self) -> int:
        return self.stack[-1][0]




