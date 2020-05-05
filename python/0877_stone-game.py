#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:57:33
# @Last Modified : 2020-05-05 22:57:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
        """DP GOOD TODO  `lru_cache`
        https://leetcode-cn.com/problems/stone-game/solution/shi-zi-you-xi-by-leetcode/
        令 dp(i, j) 为亚历克斯可以获得的最大分数,其中剩下的堆中的石子数是 piles[i], piles[i+1], ..., piles[j]
        """
        N = len(piles)
        #缓存递归调用
        @functools.lru_cache(None)
        def dp(i, j):
            print("DP(%d,%d)"%(i,j))
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j:
                return 0
            # // j - i - N; but +x = -x (mod 2)
            parity = (j + i + N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, N - 1) > 0



class Solution2(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if len(piles) % 2 == 0 or len(piles) == 1:
            return True

        dp = [0] * len(piles)
        for i in reversed(range(len(piles))):
            dp[i] = piles[i]
            for j in range(i+1, len(piles)):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[-1] >= 0

@pytest.mark.parametrize("args,expected", [
    ([5, 3, 4, 5], True),
])
def test_solutions(args, expected):
    assert Solution().stoneGame(args) == expected
    assert Solution1().stoneGame(args) == expected
    assert Solution2().stoneGame(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
