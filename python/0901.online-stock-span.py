#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 11:55:23
# @Last Modified : 2020-04-27 11:55:23
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


class StockSpanner:
    """
    单调栈
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        result = 1
        # print("Stack", self.stack)
        while self.stack and self.stack[-1][1] <= price:
            result += self.stack.pop()[0]
        self.stack.append((result, price))
        return result


if __name__ == '__main__':
    obj = StockSpanner()
    ops_list = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    args_list = [[], [100], [80], [60], [70], [60], [75], [85]]
    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
