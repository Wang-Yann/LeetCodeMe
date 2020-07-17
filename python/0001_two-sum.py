#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表
#  👍 8665 👎 0

from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, v in enumerate(nums):
            if target - v in lookup:
                return [i, lookup[target - v]]
            lookup[v] = i
        return []


@pytest.mark.parametrize("args,expected", [
    [([2, 7, 9, 11, 15], 18), [1, 3]],
    [([3, 2, 4], 6), [1, 2]]
])
def test_solutions(args, expected):
    assert sorted(Solution().twoSum(*args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
