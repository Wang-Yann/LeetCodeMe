#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 4/4/20 10:35 PM
# @Last Modified : 4/4/20 10:35 PM
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def maxSubArray0(self, nums: List[int]) -> int:
        """贪心算法"""
        temp = []
        max_sofar, max_result = float("-inf"), float("-inf")
        for v in nums:
            max_sofar = max(v, max_sofar + v)
            max_result = max(max_sofar, max_result)
            temp.append(max_result)
        print(temp)
        return max_result

    def maxSubArray(self, nums: List[int]) -> int:
        """动态规划"""
        length = len(nums)
        max_sum = nums[0]
        temp = [max_sum]
        for i in range(1, length):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
            temp.append(max_sum)
        print(temp)
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    sample = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(sol.maxSubArray0(sample))
    print(sol.maxSubArray(sample))
