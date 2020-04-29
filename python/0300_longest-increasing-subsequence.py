#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-29 21:37:52
# @Last Modified : 2020-04-29 21:37:52
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        定义 dp[i]  为考虑前 i 个元素，以第 i个数字结尾的最长上升子序列的长度，注意 nums[i] 必须被选取。
        我们从小到大计算 dp[] 数组的值，在计算  dp[i] 之前，我们已经计算出  dp[0…i−1] 的值，则状态转移方程为：
        dp[i] = max(dp[j]) + 1,  其中0<=j<=i 且  num[j]<num[i]

        """
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)


class Solution1:

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小

        """
        LIS = []

        def insert(target):
            l, r = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while l <= r:
                mid = (l + r) >> 1
                if LIS[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            # If not found, append the target.
            if l == len(LIS):
                LIS.append(target)
            else:
                LIS[l] = target

        for num in nums:
            insert(num)
        return len(LIS)


@pytest.mark.parametrize("args,expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
])
def test_solutions(args, expected):
    assert Solution().lengthOfLIS(args) == expected
    assert Solution1().lengthOfLIS(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
