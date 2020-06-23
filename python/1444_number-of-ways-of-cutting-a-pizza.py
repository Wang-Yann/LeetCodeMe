#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1
#  次，得到 k 块披萨并送给别人。 
# 
#  切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平
# 地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。 
# 
#  请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：pizza = ["A..","AAA","..."], k = 3
# 输出：3 
# 解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。
#  
# 
#  示例 2： 
# 
#  输入：pizza = ["A..","AA.","..."], k = 3
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：pizza = ["A..","A..","..."], k = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rows, cols <= 50 
#  rows == pizza.length 
#  cols == pizza[i].length 
#  1 <= k <= 10 
#  pizza 只包含字符 'A' 和 '.' 。 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        """
        HARD
        https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza/solution/dong-tai-gui-hua-by-coldme-2-2/
        """
        MOD = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        # dp[m][n][k]
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]

        # nums[i][j]: how many apples in pizza[i:][j:]
        nums = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                hasApple = pizza[i][j] == "A"
                if i == m - 1 and j == n - 1:
                    nums[i][j] = hasApple
                elif i == m - 1:
                    nums[i][j] = hasApple + nums[i][j + 1]
                elif j == n - 1:
                    nums[i][j] = hasApple + nums[i + 1][j]
                else:
                    nums[i][j] = hasApple + nums[i + 1][j] + nums[i][j + 1] - nums[i + 1][j + 1]

        # dp[i][j][p] = sum(dp[x][j][p] for x in [i+1,m-1]) + sum(dp[i][y][p] for y in [j+1, n-1])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums[i][j]:
                    dp[i][j][0] = 1
                for p in range(1, k):
                    for x in range(i + 1, m):
                        if nums[i][j] - nums[x][j]:
                            dp[i][j][p] += dp[x][j][p - 1] % MOD
                    for y in range(j + 1, n):
                        if nums[i][j] - nums[i][y]:
                            dp[i][j][p] += dp[i][y][p - 1] % MOD
        # print(nums,dp)
        return dp[0][0][k - 1] % MOD


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(pizza=["A..", "AAA", "..."], k=3), 3],
    [dict(pizza=["A..", "AA.", "..."], k=3), 1],
    [dict(pizza=["A..", "A..", "..."], k=1), 1],
])
def test_solutions(kw, expected):
    assert Solution().ways(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
