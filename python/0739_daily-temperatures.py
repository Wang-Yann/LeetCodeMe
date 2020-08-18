#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 16:15:54
# @Last Modified : 2020-04-26 16:15:54
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
#
#  例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2
# , 1, 1, 0, 0]。
#
#  提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
#  Related Topics 栈 哈希表
#  👍 441 👎 0

"""

from typing import List

import pytest


class Solution:

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        不升高  　－－　递减
        单调栈
        我们通过当前温度和栈顶索引所代表的温度比较来找到温度升高的位置
        """
        N = len(T)
        result = [0] * N
        stack = []
        for idx, v in enumerate(T):
            while stack and v > stack[-1][1]:
                pre_idx, pre_v = stack.pop()
                result[pre_idx] = idx - pre_idx
            stack.append((idx, v))
        # print(result)
        return result


@pytest.mark.parametrize("args,expected", [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]),
    pytest.param([], []),
    pytest.param([1, 3], [1, 0]),
])
def test_solutions(args, expected):
    assert Solution().dailyTemperatures(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
