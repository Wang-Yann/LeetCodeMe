#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。 
# 
#  每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。 
# 
#  给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。 
# 
#  由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：steps = 3, arrLen = 2
# 输出：4
# 解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
# 向右，向左，不动
# 不动，向右，向左
# 向右，不动，向左
# 不动，不动，不动
#  
# 
#  示例 2： 
# 
#  输入：steps = 2, arrLen = 4
# 输出：2
# 解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
# 向右，向左
# 不动，不动
#  
# 
#  示例 3： 
# 
#  输入：steps = 4, arrLen = 2
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= steps <= 500 
#  1 <= arrLen <= 10^6 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        我们用 f[i][j] 表示在进行了 i 次操作后，指针位置为 j 的方案数。由于指针在每一步操作中可以从向左移动 1 步、
        停在原地、向右移动 1 步中选择一种，因此对于状态 f[i][j]，
        它可以从 f[i - 1][j - 1]，f[i - 1][j]，f[i - 1][j + 1] 这三个状态转移而来
        """
        MOD = 10 ** 9 + 7
        N = min(arrLen, steps + 1)
        dp = [[0] * N for _ in range(steps + 1)]
        dp[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(N):
                for k in [-1, 0, 1]:
                    if 0 <= j + k < N:
                        dp[i][j] += dp[i - 1][j + k]
        # print(dp)
        return dp[steps][0] % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(steps=3, arrLen=2), 4],
    [dict(steps=2, arrLen=4), 2],
    [dict(steps=4, arrLen=2), 8],
])
def test_solutions(kw, expected):
    assert Solution().numWays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
