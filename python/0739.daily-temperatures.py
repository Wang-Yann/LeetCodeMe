#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 16:15:54
# @Last Modified : 2020-04-26 16:15:54
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        不升高  　－－　递减
        单调栈
        我们通过当前温度和栈顶索引所代表的温度比较来找到温度升高的位置
        """
        length = len(T)
        result = [0] * length
        stack = []
        for idx, v in enumerate(T):
            while stack and v>=stack[-1][1]:
                pre_idx, pre_v = stack.pop()
                result[pre_idx] = idx - pre_idx
            stack.append((idx,v))
        # print(result)
        return result


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [],
        [1, 3]

    ]
    lists = [x for x in samples]
    res = [sol.dailyTemperatures(x) for x in lists]
    print(res)
