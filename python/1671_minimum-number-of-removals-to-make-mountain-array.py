#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 02:40:58
# @Last Modified : 2021-02-23 02:40:58
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们定义 arr 是 山形数组 当且仅当它满足： 
# 
#  
#  arr.length >= 3 
#  存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
#  
#  arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#  arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 
#  
#  
#  
# 
#  给你整数数组 nums ，请你返回将 nums 变成 山形状数组 的 最少 删除次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,3,1]
# 输出：0
# 解释：数组本身就是山形数组，所以我们不需要删除任何元素。
#  
# 
#  示例 2： 
# 
#  输入：nums = [2,1,1,5,6,2,3,1]
# 输出：3
# 解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。
#  
# 
#  示例 3： 
# 
#  输入：nums = [4,3,2,1,1,2,3,1]
# 输出：4
#  
# 
#  提示： 
# 
#  输入：nums = [1,2,3,4,4,3,2,1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  1 <= nums[i] <= 109 
#  题目保证 nums 删除一些元素后一定能得到山形数组。 
#  
#  Related Topics 动态规划 
#  👍 8 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Actually, it can be done in easier way: let dp1[i] be maximum length of LIS, ending with element index i and dp2[i] be maximum length of Mountain array. Then, update of dp1 is straightforward: iterate over all previous elements and update it. For dp2[i] we again need to iterate over all previous elements and if nums[j] < nums[i], we can update dp2[i], using dp2[j] + 1 or dp1[j] + 1.

        N = len(nums)
        dp1, dp2 = [1] * N, [1] * N
        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp1[i], 1 + dp1[j])
                if nums[j] > nums[i]:
                    if dp1[j] > 1:
                        dp2[i] = max(dp2[i], 1 + dp1[j])
                    if dp2[j] > 1:
                        dp2[i] = max(dp2[i], 1 + dp2[j])

        return N - max(dp2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 3, 1]), 0],
    [dict(nums=[2, 1, 1, 5, 6, 2, 3, 1]), 3],
    [dict(nums=[4, 3, 2, 1, 1, 2, 3, 1]), 4],
    [dict(nums=[1, 2, 3, 4, 4, 3, 2, 1]), 1],
])
def test_solutions(kw, expected):
    assert Solution().minimumMountainRemovals(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
