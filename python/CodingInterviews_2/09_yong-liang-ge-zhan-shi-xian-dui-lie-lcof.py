#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:47:11
# @Last Modified : 2020-04-23 23:47:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的
# 功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
#
#
#  示例 1：
#
#  输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
#
#
#  示例 2：
#
#  输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
#
#
#  提示：
#
#
#  1 <= values <= 10000
#  最多会对 appendTail、deleteHead 进行 10000 次调用
#
#  Related Topics 栈 设计
#  👍 91 👎 0

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
