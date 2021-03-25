#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 16:34:43
# @Last Modified : 2020-04-12 16:34:43
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#  Related Topics 数组 回溯算法
#  👍 269 👎 0

"""

from typing import List

import pytest


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            回溯
            TODO absorb
        """
        nums.sort()

        def backtrack(first, curr, k):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                if i > first and nums[i] == nums[i - 1]:
                    continue
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr, k)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0, [], k)
        return output


@pytest.mark.parametrize("args,expected", [
    [[1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]],
    [[2, 1, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]],
    [[1, 5, 3, 6],
     [[], [1], [3], [5], [6], [1, 3], [1, 5], [1, 6], [3, 5],
      [3, 6], [5, 6], [1, 3, 5], [1, 3, 6], [1, 5, 6],
      [3, 5, 6], [1, 3, 5, 6]]],
])
def test_solutions(args, expected):
    assert Solution().subsetsWithDup(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
