#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-22 02:56:26
# @Last Modified : 2021-03-22 02:56:26
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。 
# 
#  在第 i 次操作时（操作编号从 1 开始），你需要： 
# 
#  
#  选择两个元素 x 和 y 。 
#  获得分数 i * gcd(x, y) 。 
#  将 x 和 y 从 nums 中删除。 
#  
# 
#  请你返回 n 次操作后你能获得的分数和最大为多少。 
# 
#  函数 gcd(x, y) 是 x 和 y 的最大公约数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2]
# 输出：1
# 解释：最优操作是：
# (1 * gcd(1, 2)) = 1
#  
# 
#  示例 2： 
# 
#  输入：nums = [3,4,6,8]
# 输出：11
# 解释：最优操作是：
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
#  
# 
#  示例 3： 
# 
#  输入：nums = [1,2,3,4,5,6]
# 输出：14
# 解释：最优操作是：
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 7 
#  nums.length == 2 * n 
#  1 <= nums[i] <= 106 
#  
#  Related Topics 递归 动态规划 回溯算法 
#  👍 8 👎 0


import functools
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """状压DP"""
        N = len(nums)

        @functools.lru_cache(None)
        def cache_gcd(x, y):
            return math.gcd(x, y)

        @functools.lru_cache(None)
        def dfs(rnd, mask):
            if rnd > N // 2:
                return 0
            res = 0
            for i in range(N):
                for j in range(i + 1, N):
                    new_mask = (1 << i) | (1 << j)
                    if not mask & new_mask:
                        res = max(res, rnd * cache_gcd(nums[i], nums[j]) + dfs(rnd + 1, new_mask | mask))
            return res

        return dfs(1, 0)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2]), 1],
    [dict(nums=[3, 4, 6, 8]), 11],
    [dict(nums=[1, 2, 3, 4, 5, 6]), 14],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxScore(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
