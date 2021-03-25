#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-14 21:27:39
# @Last Modified : 2020-04-14 21:27:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#  示例:
#
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6
#  Related Topics 栈 数组 哈希表 动态规划
#  👍 517 👎 0

"""

from typing import List

import pytest


class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights):
            increasing_stack, area, i = [], 0, 0
            length = len(heights)
            while i <= length:
                if not increasing_stack or (i < length and heights[i] > heights[increasing_stack[-1]]):
                    increasing_stack.append(i)
                    i += 1
                else:
                    last_pos = increasing_stack.pop()
                    if not increasing_stack:
                        area = max(area, heights[last_pos] * i)
                    else:
                        area = max(area, heights[last_pos] * (i - increasing_stack[-1] - 1))
            return area

        if not matrix:
            return 0
        result = 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        for row in range(m):
            for col in range(n):
                heights[col] = heights[col] + 1 if matrix[row][col] == "1" else 0
            result = max(result, largestRectangleArea(heights))
        return result


@pytest.mark.parametrize("args,expected", [
    ([
         ["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]
     ], 6)
])
def test_solutions(args, expected):
    assert Solution().maximalRectangle(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
