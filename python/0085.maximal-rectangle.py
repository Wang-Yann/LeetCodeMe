#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-14 21:27:39
# @Last Modified : 2020-04-14 21:27:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]

    ]
    res = [sol.maximalRectangle(x) for x in samples]
    print(res)
