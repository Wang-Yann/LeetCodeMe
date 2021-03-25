#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40 。 
# 
#  给你一个整数列表的列表 hats ，其中 hats[i] 是第 i 个人所有喜欢帽子的列表。 
# 
#  请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。 
# 
#  由于答案可能很大，请返回它对 10^9 + 7 取余后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：hats = [[3,4],[4,5],[5]]
# 输出：1
# 解释：给定条件下只有一种方法选择帽子。
# 第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。 
# 
#  示例 2： 
# 
#  
# 输入：hats = [[3,5,1],[3,5]]
# 输出：4
# 解释：总共有 4 种安排帽子的方法：
# (3,5)，(5,3)，(1,3) 和 (1,5)
#  
# 
#  示例 3： 
# 
#  
# 输入：hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# 输出：24
# 解释：每个人都可以从编号为 1 到 4 的帽子中选。
# (1,2,3,4) 4 个帽子的排列方案数为 24 。
#  
# 
#  示例 4： 
# 
#  
# 输入：hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
# 输出：111
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == hats.length 
#  1 <= n <= 10 
#  1 <= hats[i].length <= 40 
#  1 <= hats[i][j] <= 40 
#  hats[i] 包含一个数字互不相同的整数列表。 
#  
#  Related Topics 位运算 动态规划

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # 总人数
        MOD = 10 ** 9 + 7
        N = len(hats)

        @functools.lru_cache(None)
        def dp(cur, pos):
            # cur 代表当前轮到第cur顶帽子可供选择
            # pos 代表当前戴帽的人有哪些，为二进制压缩状态形式
            # 首先，如果当前所有人都带上了帽，则返回1
            if pos == (1 << N) - 1:
                return 1
            # 若不满足所有人都戴上了帽，且当前也没有帽子了，则返回0
            if cur > 40:
                return 0
            # 首先考虑不戴该顶帽子，直接考虑后一顶，则其值应为dp(cur+1, pos)
            res = dp(cur + 1, pos)
            # 考虑有人佩戴该顶帽子
            for i in range(N):
                # 找到喜欢该帽子的人，且这个人并没有戴其他帽子（即二进制pos中该位置为0）
                if cur in hats[i] and not pos & (1 << i):
                    # 给这个人戴上帽子（该位置置1），并依序进行下去
                    res += dp(cur + 1, pos + (1 << i))
            return res % MOD

        return dp(0, 0)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def numberWays(self, hats: List[List[int]]) -> int:
        """ 状压DP"""
        MOD = 10 ** 9 + 7
        HAT_SIZE = 40
        N = len(hats)
        hat_to_people = [[] for _ in range(HAT_SIZE)]
        for i in range(N):
            for h in hats[i]:
                hat_to_people[h - 1].append(i)
        dp = [0] * (1 << N)
        dp[0] = 1
        for people in hat_to_people:
            for mask in range(len(dp) - 1, -1, -1):
                for p in people:
                    if mask & (1 << p):
                        continue
                    dp[mask | (1 << p)] += dp[mask]
                    dp[mask | (1 << p)] %= MOD
        # print(dp)
        return dp[-1]


@pytest.mark.parametrize("kw,expected", [
    [dict(hats=[[3, 4], [4, 5], [5]]), 1],
    [dict(hats=[[3, 5, 1], [3, 5]]), 4],
    [dict(hats=[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]), 24],
    [dict(hats=[[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]), 111],
])
def test_solutions(kw, expected):
    assert Solution().numberWays(**kw) == expected
    assert Solution1().numberWays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
