#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:22:12
# @Last Modified : 2020-05-05 15:22:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。
#
#
#
#  示例:
#
#  输入:
# [1,2,3]
#
# 输出:
# 3
#
# 解释:
# 只需要3次移动（注意每次移动会增加两个元素的值）：
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#
#  Related Topics 数学
#  👍 128 👎 0

"""

from typing import List

import pytest


class Solution:

    def minMoves(self, nums: List[int]) -> int:
        """
        Good
        将除了一个元素之外的全部元素+1，等价于将该元素-1，因为我们只对元素的相对大小感兴趣。因此，该问题简化为需要进行的减法次数。
        我们只需要将所有的数都减到最小的数即可
        """
        return sum(nums) - len(nums) * min(nums)


class Solution1:

    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums) - 1, 0, -1):
            cnt += nums[i] - nums[0]
        return cnt


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3], 3),
])
def test_solutions(args, expected):
    assert Solution().minMoves(args) == expected
    assert Solution1().minMoves(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
