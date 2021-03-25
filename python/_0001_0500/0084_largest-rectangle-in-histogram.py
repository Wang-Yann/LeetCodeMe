#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-13 22:27:19
# @Last Modified : 2020-04-13 22:27:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
#  示例:
#
#  输入: [2,1,5,6,2,3]
# 输出: 10
#  Related Topics 栈 数组
#  👍 798 👎 0

"""

from typing import List

import pytest


class Solution:
    """
    TODO 单调栈
    push 进去之前先把 >= 自己的元素 pop 出来。
每次从栈中 pop 出一个数的时候，就找到了往左数比它小的第一个数（当前栈顶）和往右数比它小的第一个数（即将入栈的数），
从而可以计算出这两个数中间的部分宽度 * 被pop出的数，就是以这个被pop出来的数为最低的那个直方向两边展开的最大矩阵面积
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []  # stores increasing height

        i = 0
        while i < len(heights) + 1:
            if not stack or (i < len(heights) and heights[i] > heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                last_pos = stack.pop()
                if not stack:
                    result = max(result, heights[last_pos] * i)
                else:
                    result = max(result, heights[last_pos] * (i - stack[-1] - 1))

        return result


class Solution1:

    def calculateArea(self, heights: List[int], start: int, end: int) -> int:
        if start > end:
            return 0
        min_index = start
        for i in range(start, end + 1):
            if heights[min_index] > heights[i]:
                min_index = i
        return max(heights[min_index] * (end - start + 1),
                   self.calculateArea(heights, start, min_index - 1),
                   self.calculateArea(heights, min_index + 1, end)
                   )

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.calculateArea(heights, 0, len(heights) - 1)


class Solution2:

    def largestRectangleArea(self, heights: List[int]) -> int:
        A = heights
        result = 0
        stack = [-1]

        for i in range(len(A)):
            while stack[-1] != -1 and A[i] <= A[stack[-1]]:
                last_pos = stack.pop()
                result = max(result, A[last_pos] * (i - stack[-1] - 1))
            stack.append(i)
            # 当我们到达数组的尾部时，我们将栈中剩余元素全部弹出栈
        while stack and stack[-1] != -1:
            last_pos = stack.pop()
            result = max(result, A[last_pos] * (len(A) - stack[-1] - 1))
        return result


@pytest.mark.parametrize("args,expected", [
    ([2, 1, 5, 6, 2, 3], 10),
    pytest.param([], 0),
])
def test_solutions(args, expected):
    assert Solution().largestRectangleArea(args) == expected
    assert Solution1().largestRectangleArea(args) == expected
    assert Solution2().largestRectangleArea(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
