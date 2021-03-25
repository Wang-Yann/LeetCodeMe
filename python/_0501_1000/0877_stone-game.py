#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:57:33
# @Last Modified : 2020-05-05 22:57:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
#
#  游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
#
#  亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
#
#
#  假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
#
#
#
#  示例：
#
#  输入：[5,3,4,5]
# 输出：true
# 解释：
# 亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
# 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
# 如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
# 如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
# 这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
#
#
#
#
#  提示：
#
#
#  2 <= piles.length <= 500
#  piles.length 是偶数。
#  1 <= piles[i] <= 500
#  sum(piles) 是奇数。
#
#  Related Topics 极小化极大 数学 动态规划
#  👍 153 👎 0

"""
import functools
from typing import List

import pytest


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        """
        显然，亚历克斯总是赢得 2 堆时的游戏。 通过一些努力，我们可以获知她总是赢得 4 堆时的游戏。
        如果亚历克斯最初获得第一堆，她总是可以拿第三堆。 如果她最初取到第四堆，她总是可以取第二堆。
        第一 + 第三，第二 + 第四 中的至少一组是更大的，所以她总能获胜。

        我们可以将这个想法扩展到 N 堆的情况下。设第一、第三、第五、第七桩是白色的，第二、第四、第六、第八桩是黑色的。
         亚历克斯总是可以拿到所有白色桩或所有黑色桩，其中一种颜色具有的石头数量必定大于另一种颜色的


        """
        return True


class Solution1:

    def stoneGame(self, piles: List[int]) -> bool:
        """DP GOOD
        TODO  `lru_cache`
        https://leetcode-cn.com/problems/stone-game/solution/shi-zi-you-xi-by-leetcode/
        令 dp(i, j) 为亚历克斯可以获得的最大分数,其中剩下的堆中的石子数是 piles[i], piles[i+1], ..., piles[j]
        """
        N = len(piles)

        # 缓存递归调用
        @functools.lru_cache(None)
        def dp(i, j):
            # print("DP(%d,%d)"%(i,j))
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j:
                return 0
            # // j - i - N; but +x = -x (mod 2)
            parity = (j + i + N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, N - 1) > 0


class Solution2(object):
    def stoneGame(self, piles):
        N = len(piles)
        if N % 2 == 0 or N == 1:
            return True

        dp = [0] * N
        for i in range(N - 1, -1, -1):
            dp[i] = piles[i]
            for j in range(i + 1, N):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[N - 1] >= 0


class Pair(object):
    __slots__ = "fir", "sec"

    def __init__(self, fir, sec):
        self.fir = fir
        self.sec = sec


class Solution3(object):
    """
    二维通用
        dp[i][j].fir 表示，对于 piles[i...j] 这部分石头堆，先手能获得的最高分数。
        dp[i][j].sec 表示，对于 piles[i...j] 这部分石头堆，后手能获得的最高分数

    """

    def stoneGame(self, piles):
        N = len(piles)
        dp = [[Pair(0, 0)] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            dp[i][i].fir = piles[i]
        for l in range(2, N + 1):
            for i in range(N + 1 - l):
                j = l + i - 1
                # // 先手选择最左边或最右边的分数
                # 我作为先手，面对 piles[i...j] 时，有两种选择：
                # # 要么我选择最左边的那一堆石头，然后面对 piles[i+1...j]
                # # 但是此时轮到对方，相当于我变成了后手；
                # # 要么我选择最右边的那一堆石头，然后面对 piles[i...j-1]
                # # 但是此时轮到对方，相当于我变成了后手。
                left = piles[i] + dp[i + 1][j].sec
                right = piles[j] + dp[i][j - 1].sec
                if left > right:
                    dp[i][j].fir = left
                    dp[i][j].sec = dp[i + 1][j].fir
                else:
                    dp[i][j].fir = right
                    dp[i][j].sec = dp[i][j - 1].fir
        return dp[0][N].fir - dp[0][N].sec > 0


@pytest.mark.parametrize("args,expected", [
    ([5, 3, 4, 5], True),
    ([5, 3, 4, 5, 9, 7], True),
])
def test_solutions(args, expected):
    assert Solution().stoneGame(args) == expected
    assert Solution1().stoneGame(args) == expected
    assert Solution2().stoneGame(args) == expected
    assert Solution3().stoneGame(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
