#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 03:55:24
# @Last Modified : 2021-02-26 03:55:24
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，爱丽丝先开始 。 
# 
#  有 n 块石子排成一排。每个玩家的回合中，可以从行中 移除 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 和 相等的得分。当没有石头可移除时，得
# 分较高者获胜。 
# 
#  鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 减小得分的差值 。爱丽丝的目标是最大限度地 扩大得分的差值 。 
# 
#  给你一个整数数组 stones ，其中 stones[i] 表示 从左边开始 的第 i 个石头的值，如果爱丽丝和鲍勃都 发挥出最佳水平 ，请返回他们 得分
# 的差值 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：stones = [5,3,1,4,2]
# 输出：6
# 解释：
# - 爱丽丝移除 2 ，得分 5 + 3 + 1 + 4 = 13 。游戏情况：爱丽丝 = 13 ，鲍勃 = 0 ，石子 = [5,3,1,4] 。
# - 鲍勃移除 5 ，得分 3 + 1 + 4 = 8 。游戏情况：爱丽丝 = 13 ，鲍勃 = 8 ，石子 = [3,1,4] 。
# - 爱丽丝移除 3 ，得分 1 + 4 = 5 。游戏情况：爱丽丝 = 18 ，鲍勃 = 8 ，石子 = [1,4] 。
# - 鲍勃移除 1 ，得分 4 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [4] 。
# - 爱丽丝移除 4 ，得分 0 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [] 。
# 得分的差值 18 - 12 = 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：stones = [7,90,5,1,100,10,10,2]
# 输出：122 
# 
#  
# 
#  提示： 
# 
#  
#  n == stones.length 
#  2 <= n <= 1000 
#  1 <= stones[i] <= 1000 
#  
#  Related Topics 动态规划 
#  👍 40 👎 0


import functools
import itertools
import sys
from typing import List

import pytest

from sample_datas import BIG_1690

sys.setrecursionlimit(10 ** 5)


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
       
        N = len(stones)
        dp = [[0] * N for _ in range(N)]
        p_sum = [0] + list(itertools.accumulate(stones))
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = max(p_sum[j + 1] - p_sum[i + 1] - dp[i + 1][j],
                               p_sum[j] - p_sum[i] - dp[i][j - 1])
        return dp[0][N - 1]


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def stoneGameVII(self, stones: List[int]) -> int:
        """
        Time Limit Exceeded
        memoise the results for the start (i) and end(j) of the remaining stones
        """
        p_sum = [0] + list(itertools.accumulate(stones))

        @functools.lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0
            sum_val = p_sum[j + 1] - p_sum[i]
            return max(sum_val - stones[i] - dp(i + 1, j), sum_val - stones[j] - dp(i, j - 1))

        res = dp(0, len(stones) - 1)
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(stones=[5, 3, 1, 4, 2]), 6],
    [dict(stones=[7, 90, 5, 1, 100, 10, 10, 2]), 122],
    [dict(stones=BIG_1690.BIG_INPUT), 227354],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().stoneGameVII(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
