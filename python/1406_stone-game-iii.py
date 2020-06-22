#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# Alice 和 Bob 用几堆石子在做游戏。几堆石子排成一行，每堆石子都对应一个得分，由数组 stoneValue 给出。 
# 
#  Alice 和 Bob 轮流取石子，Alice 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子 。比赛一直持续到所
# 有石头都被拿走。 
# 
#  每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 0 。比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平
# 局。 
# 
#  假设 Alice 和 Bob 都采取 最优策略 。如果 Alice 赢了就返回 "Alice" ，Bob 赢了就返回 "Bob"，平局（分数相同）返回 "
# Tie" 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：values = [1,2,3,7]
# 输出："Bob"
# 解释：Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
#  
# 
#  示例 2： 
# 
#  输入：values = [1,2,3,-9]
# 输出："Alice"
# 解释：Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
# 如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9 的石子堆，输掉比赛。
# 
# 如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9 的石子堆，同样会输掉比赛。
# 
# 注意，他们都应该采取 最优策略 ，所以在这里 Alice 将选择能够使她获胜的方案。 
# 
#  示例 3： 
# 
#  输入：values = [1,2,3,6]
# 输出："Tie"
# 解释：Alice 无法赢得比赛。如果她决定选择前三堆，她可以以平局结束比赛，否则她就会输。
#  
# 
#  示例 4： 
# 
#  输入：values = [1,2,3,-1,-2,-3,7]
# 输出："Alice"
#  
# 
#  示例 5： 
# 
#  输入：values = [-1,-2,-3]
# 输出："Tie"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= values.length <= 50000 
#  -1000 <= values[i] <= 1000 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        https://leetcode-cn.com/problems/stone-game-iii/solution/python-ping-deng-bo-yi-dp-by-littledva/
        """
        sum_val = 0
        N = len(stoneValue)
        dp = [0] * (N + 3) 
        for i in range(len(stoneValue) - 1, -1, -1):
            sum_val += stoneValue[i]
            choose = min(dp[i + 1], dp[i + 2], dp[i + 3])
            dp[i] = sum_val - choose
        # print(dp)
        if dp[0] + dp[0] < sum_val:
            return "Bob"
        elif dp[0] + dp[0] > sum_val:
            return "Alice"
        else:
            return "Tie"


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(stoneValue=[1, 2, 3, 7]), "Bob"],
    [dict(stoneValue=[1, 2, 3, -9]), "Alice"],
    [dict(stoneValue=[1, 2, 3, 6]), "Tie"],
    [dict(stoneValue=[1, 2, 3, -1, -2, -3, 7]), "Alice"],
    [dict(stoneValue=[-1, -2, -3]), "Tie"],
])
def test_solutions(kw, expected):
    assert Solution().stoneGameIII(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
