#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 19:36:06
# @Last Modified : 2020-04-25 19:36:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


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
