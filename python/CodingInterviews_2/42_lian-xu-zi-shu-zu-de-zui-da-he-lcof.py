#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 17:59:35
# @Last Modified : 2020-05-10 17:59:35
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
#  要求时间复杂度为O(n)。
#
#
#
#  示例1:
#
#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 10^5
#  -100 <= arr[i] <= 100
#
#
#  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/
#
#
#  Related Topics 分治算法 动态规划
#  👍 83 👎 0


import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_cur,ans =float("-inf"),float("-inf")
        for v in nums:
            max_cur = max(v,max_cur+v)
            ans = max(ans,max_cur)
        return ans


@pytest.mark.parametrize("args,expected", [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
])
def test_solutions(args, expected):
    assert Solution().maxSubArray(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


