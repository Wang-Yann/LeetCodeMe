#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 17:46:14
# @Last Modified : 2020-04-29 17:46:14
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
"""
一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

 

编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

说明:

骑士的健康点数没有上限。

任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。


"""

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
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dpmin = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, dpmin - dungeon[i][j])
        # print(dp)
        return dp[0][0]


class Solution1:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        BIG = 10 ** 9
        dp = [[BIG] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]


@pytest.mark.parametrize("args,expected", [
    ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7)
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.calculateMinimumHP(args) == expected
    sol = Solution1()
    assert sol.calculateMinimumHP(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
