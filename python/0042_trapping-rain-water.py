#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-07 21:42:49
# @Last Modified : 2020-04-07 21:42:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。
#
#
#
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marco
# s 贡献此图。
#
#  示例:
#
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#  Related Topics 栈 数组 双指针
#  👍 18 👎 0


from typing import List

import pytest


class Solution:
    def trap(self, height: List[int]) -> int:
        """单调栈"""
        ans = 0
        stack = []
        for r in range(len(height)):
            while stack and height[r] > height[stack[-1]]:
                cur_pos = stack.pop()
                if not stack:
                    break
                l = stack[-1]
                cur_h = min(height[l], height[r]) - height[cur_pos]
                ans += cur_h * (r - l - 1)
            stack.append(r)

        return ans


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
])
def test_solutions(args, expected):
    assert Solution().trap(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
