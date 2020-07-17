#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 23:18:39
# @Last Modified : 2020-04-25 23:18:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 使用队列实现栈的下列操作：
#
#
#  push(x) -- 元素 x 入栈
#  pop() -- 移除栈顶元素
#  top() -- 获取栈顶元素
#  empty() -- 返回栈是否为空
#
#
#  注意:
#
#
#  你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合
# 法的。
#  你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
#  你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
#
#  Related Topics 栈 设计
#  👍 197 👎 0

class MyStack0:
    """双队列"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left_q = []
        self.right_q = []
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.left_q.append(x)
        self._top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.left_q) > 1:
            self._top = self.left_q.pop(0)
            self.right_q.append(self._top)
        ret = self.left_q.pop(0)
        self.left_q, self.right_q = self.right_q, self.left_q
        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.left_q and not self.right_q


class MyStack:
    """单队列"""

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        self._top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(len(self.q) - 1):
            self._top = self.q.pop(0)
            self.q.append(self._top)
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q


if __name__ == '__main__':
    obj = MyStack()
    obj.push(12)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
