#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 18:24:57
# @Last Modified : 2020-04-26 18:24:57
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for char in ops:
            if char == "C":
                stack.pop()
            elif char == "D":
                v = stack[-1] * 2
                stack.append(v)
            elif char == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(char))
        # print("stack",stack)
        return sum(stack)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        # ["5", "2", "C", "D", "+"],
        ["5", "-2", "4", "C", "D", "9", "+", "+"],
        ["57", "D", "-3", "-58", "D", "77", "+", "C", "+", "+", "38", "78", "-6", "24", "-46", "+",
         "31", "20", "D", "-81"]

    ]
    lists = [x for x in samples]
    res = [sol.calPoints(x) for x in lists]
    print(res)
