#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 23:11:11
# @Last Modified : 2020-04-25 23:11:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
from typing import List


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left_stack = []
        self.right_stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.left_stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.right_stack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.right_stack:
            return self.right_stack[-1]
        elif self.left_stack:
            while self.left_stack:
                val = self.left_stack.pop()
                self.right_stack.append(val)
            return self.right_stack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.left_stack and not self.right_stack

if __name__ == '__main__':
    obj = MyQueue()
    obj.push(12)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()