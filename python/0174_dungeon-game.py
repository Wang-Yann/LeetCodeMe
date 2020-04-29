#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 17:46:14
# @Last Modified : 2020-04-29 17:46:14
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        仔细想想,不是简单的DP
        #####DP含义是思考重点
        用 dp[i][j] 存储从起点 (0, 0) 到达 (i, j) 到达终点所需要的最小生命值。
        此时dp[i][j]的含义为：至少的血量，并且这个血量必须大于1。如果你到这的时候已经是1，
        那么至少就选1，如果你到这的血量小于1，那么此时的血量必须为1，。
        然后当地牢为一格的时候，dp = max(1, 1 - dungeon[0][0]);
        dungeon为正的时候dp取1，dungeon为负的时候，dp = 1 - dungeon;
        然后初始化最右侧和最下侧的地牢。
        然后就可以初始化其他层次。
        dp[i][j] = Math.max(1, Math.min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]);

        链接：https://leetcode-cn.com/problems/dungeon-game/solution/dong-tai-gui-hua-by-wisemove-2-7/

        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = max(1,1-dungeon[m-1][n-1])
        for i in range(m-2,-1,-1):
            dp[i][n-1] = max(1,dp[i+1][n-1]-dungeon[i][n-1])
        for j in range(n-2,-1,-1):
            dp[m-1][j]=max(1,dp[m-1][j+1]-dungeon[m-1][j])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dpmin = min(dp[i+i][j],dp[i][j+1])
                dp[i][j] = max(1,dpmin-dungeon[i][j])
        print(dp)
        return dp[0][0]



@pytest.mark.parametrize("args,expected", [
    ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]
      ], 7)
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.calculateMinimumHP(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
