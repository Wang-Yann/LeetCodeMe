#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 21:03:15
# @Last Modified : 2021-02-27 21:03:15
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个长度分别 n 和 m 的整数数组 nums 和 multipliers ，其中 n >= m ，数组下标 从 1 开始 计数。 
# 
#  初始时，你的分数为 0 。你需要执行恰好 m 步操作。在第 i 步操作（从 1 开始 计数）中，需要： 
# 
#  
#  选择数组 nums 开头处或者末尾处 的整数 x 。 
#  你获得 multipliers[i] * x 分，并累加到你的分数中。 
#  将 x 从数组 nums 中移除。 
#  
# 
#  在执行 m 步操作后，返回 最大 分数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3], multipliers = [3,2,1]
# 输出：14
# 解释：一种最优解决方案如下：
# - 选择末尾处的整数 3 ，[1,2,3] ，得 3 * 3 = 9 分，累加到分数中。
# - 选择末尾处的整数 2 ，[1,2] ，得 2 * 2 = 4 分，累加到分数中。
# - 选择末尾处的整数 1 ，[1] ，得 1 * 1 = 1 分，累加到分数中。
# 总分数为 9 + 4 + 1 = 14 。 
# 
#  示例 2： 
# 
#  输入：nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# 输出：102
# 解释：一种最优解决方案如下：
# - 选择开头处的整数 -5 ，[-5,-3,-3,-2,7,1] ，得 -5 * -10 = 50 分，累加到分数中。
# - 选择开头处的整数 -3 ，[-3,-3,-2,7,1] ，得 -3 * -5 = 15 分，累加到分数中。
# - 选择开头处的整数 -3 ，[-3,-2,7,1] ，得 -3 * 3 = -9 分，累加到分数中。
# - 选择末尾处的整数 1 ，[-2,7,1] ，得 1 * 4 = 4 分，累加到分数中。
# - 选择末尾处的整数 7 ，[-2,7] ，得 7 * 6 = 42 分，累加到分数中。
# 总分数为 50 + 15 - 9 + 4 + 42 = 102 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  m == multipliers.length 
#  1 <= m <= 103 
#  m <= n <= 105 
#  -1000 <= nums[i], multipliers[i] <= 1000 
#  
#  Related Topics 动态规划 
#  👍 31 👎 0
  

"""

import functools
import sys
from typing import List

import pytest

from sample_datas import BIG_1770

# leetcode submit region begin(Prohibit modification and deletion)

sys.setrecursionlimit(10 ** 5)


class Solution:

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        l  is the index of the left side
        i is the number of elements that we picked
        """
        N, M = len(nums), len(multipliers)

        # TODO @functools.lru_cache(None) 不能过!!
        @functools.lru_cache(2000)
        def dp(l, idx):
            if idx >= M:
                return 0
            pick_left = dp(l + 1, idx + 1) + nums[l] * multipliers[idx]
            pick_right = dp(l, idx + 1) + nums[N - 1 - (idx - l)] * multipliers[idx]
            return max(pick_left, pick_right)

        return dp(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @functools.lru_cache(2000)
        def dp(lo, hi, k):
            """Return max score from nums[lo:hi+1]."""
            if k == len(multipliers):
                return 0
            return max(nums[lo] * multipliers[k] + dp(lo + 1, hi, k + 1), nums[hi] * multipliers[k] + dp(lo, hi - 1, k + 1))

        return dp(0, len(nums) - 1, 0)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 3], multipliers=[3, 2, 1]), 14],
    [dict(nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]), 102],
    [dict(nums=BIG_1770.BIG_INPUT_NUMS, multipliers=BIG_1770.BIG_INPUT_M), -60234066],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().maximumScore(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
