#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:47:11
# @Last Modified : 2020-04-23 23:47:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class CQueue:

    def __init__(self):
        self.length = 10
        self.left_stack = []
        self.right_stack = []

    def appendTail(self, value: int) -> None:
        self.left_stack.append(value)

    def deleteHead(self) -> int:
        if self.right_stack:
            return self.right_stack.pop()
        elif self.left_stack:
            while self.left_stack:
                val = self.left_stack.pop()
                self.right_stack.append(val)
            return self.right_stack.pop()
        else:
            return -1


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(12)
    param_2 = obj.deleteHead()
