#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 23:11:11
# @Last Modified : 2020-04-25 23:11:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 使用栈实现队列的下列操作：
#
#
#  push(x) -- 将一个元素放入队列的尾部。
#  pop() -- 从队列首部移除元素。
#  peek() -- 返回队列首部的元素。
#  empty() -- 返回队列是否为空。
#
#
#
#
#  示例:
#
#  MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
#
#
#
#  说明:
#
#
#  你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
#
#  你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
#  假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
#
#  Related Topics 栈 设计
#  👍 197 👎 0

"""

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