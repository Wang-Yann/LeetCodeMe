#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 16:43:04
# @Last Modified : 2020-04-30 16:43:04
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
#
# 注意:
# 数组长度 n 满足以下条件:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 示例:
#
# 输入:
# nums = [7,2,5,10,8]
# m = 2
#
# 输出:
# 18
#
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。


from typing import List

import pytest


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        TODO
        https://leetcode-cn.com/problems/split-array-largest-sum/solution/410-by-ikaruga/
        """

        def canSplit(nums, m, split_sum):
            cnt, cur_sum = 1, 0
            for num in nums:
                cur_sum += num
                if cur_sum > split_sum:
                    cur_sum = num
                    cnt += 1
            return cnt <= m

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) >> 1
            if canSplit(nums, m, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


@pytest.mark.parametrize("kw,expected", [
    (dict(nums=[7, 2, 5, 10, 8],
          m=2), 18)
])
def test_solutions(kw, expected):
    assert Solution().splitArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
