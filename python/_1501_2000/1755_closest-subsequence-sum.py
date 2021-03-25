#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 10:03:56
# @Last Modified : 2021-02-23 10:03:56
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 和一个目标值 goal 。 
# 
#  你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum -
#  goal) 。 
# 
#  返回 abs(sum - goal) 可能的 最小值 。 
# 
#  注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [5,-7,3,5], goal = 6
# 输出：0
# 解释：选择整个数组作为选出的子序列，元素和为 6 。
# 子序列和与目标值相等，所以绝对差为 0 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [7,-9,15,-2], goal = -5
# 输出：1
# 解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
# 绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
#  
# 
#  示例 3： 
# 
#  输入：nums = [1,2,3], goal = -7
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 40 
#  -107 <= nums[i] <= 107 
#  -109 <= goal <= 109 
#  
#  Related Topics 分治算法 
#  👍 27 👎 0

"""

import bisect
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # function that generates all possible sums of sebsequences
        def dfs(i, cur, arr, sums):
            if i == len(arr):
                sums.add(cur)
                return
            dfs(i + 1, cur, arr, sums)
            dfs(i + 1, cur + arr[i], arr, sums)

        sums1, sums2 = set(), set()
        # generate all possible sums of the 1st and 2nd half
        dfs(0, 0, nums[:len(nums) // 2], sums1)
        dfs(0, 0, nums[len(nums) // 2:], sums2)

        # sort the possible sums of the 2nd half
        s2 = sorted(sums2)
        ans = 0x7fffffff
        # for each possible sum of the 1st half, find the sum in the 2nd half
        # that gives a value closest to the goal using binary search
        for s in sums1:
            remain = goal - s
            # binary search for the value in s2 that's closest to the remaining value
            i2 = bisect.bisect_left(s2, remain)
            if i2 < len(s2):
                ans = min(ans, abs(remain - s2[i2]))
            if i2 > 0:
                ans = min(ans, abs(remain - s2[i2 - 1]))
            # else:
            #     print(i2)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:

        def helper(nums):
            ans = {0}
            for x in nums:
                ans |= {x + y for y in ans}
            return ans

        nums0 = sorted(helper(nums[:len(nums) // 2]))
        nums1 = helper(nums[len(nums) // 2:])

        ans = math.inf
        for x in nums1:
            k = bisect.bisect_left(nums0, goal - x)
            if k < len(nums0):
                ans = min(ans, nums0[k] + x - goal)
            if k > 0:
                ans = min(ans, goal - x - nums0[k - 1])
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[9152249, 8464156, -2493402, 8990685, -7257152,
                -1050240, 2243737, -82901, 8939692], goal=26915229), 8405],
    [dict(nums=[5, -7, 3, 5], goal=6), 0],
    [dict(nums=[7, -9, 15, -2], goal=-5), 1],
    [dict(nums=[1, 2, 3], goal=-7), 7],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().minAbsDifference(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
