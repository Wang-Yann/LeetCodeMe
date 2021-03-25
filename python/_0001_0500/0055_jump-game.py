#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-08 22:47:01
# @Last Modified : 2020-04-08 22:47:01
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  判断你是否能够到达最后一个位置。
#
#  示例 1:
#
#  输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#
#
#  示例 2:
#
#  输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
#  Related Topics 贪心算法 数组
#  👍 741 👎 0

"""
from typing import List

import pytest


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res_queue = [0]
        l = len(nums)
        while res_queue:
            v = res_queue.pop()
            max_v = v + nums[v]
            if max_v >= l - 1:
                return True
            for j in range(v + 1, max_v + 1):
                if nums[j] and nums[j] + j > max_v:
                    res_queue.append(j)
        return False


class Solution1:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(last_pos - 1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


@pytest.mark.parametrize("args,expected", [
    ([2, 3, 1, 1, 4], True),
    ([8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 0, 0, 3, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6,
      5, 1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8,
      5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5], True),
    ([2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0,
      3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7,
      1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6], False),
])
def test_solutions(args, expected):
    assert Solution().canJump(args) == expected
    assert Solution1().canJump(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
