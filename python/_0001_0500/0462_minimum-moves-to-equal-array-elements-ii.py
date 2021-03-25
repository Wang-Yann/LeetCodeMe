#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:35:18
# @Last Modified : 2020-05-05 15:35:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。
#
#  例如:
#
#
# 输入:
# [1,2,3]
#
# 输出:
# 2
#
# 说明：
# 只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）：
#
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#
#  Related Topics 数学
#  👍 83 👎 0

from typing import List

import pytest


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3], 2),
    ([1, 0, 0, 8, 6], 14),
])
def test_solutions(args, expected):
    assert Solution().minMoves2(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
