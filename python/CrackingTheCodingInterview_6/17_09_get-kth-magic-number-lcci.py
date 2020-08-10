#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 21:46:26
# @Last Modified : 2020-04-27 21:46:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，
# 5，7，9，15，21。
#
#  示例 1:
#
#  输入: k = 5
#
# 输出: 9
#
#  Related Topics 堆 队列 数学
#  👍 26 👎 0
import pytest


class Solution:

    def getKthMagicNumber(self, k: int) -> int:
        p3, p5, p7 = 0, 0, 0
        dp = [1] + [0] * (k - 1)
        for i in range(1, k):
            dp3, dp5, dp7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(dp3, dp5, dp7)
            if dp3 == dp[i]:
                p3 += 1
            if dp5 == dp[i]:
                p5 += 1
            if dp7 == dp[i]:
                p7 += 1
        return dp[k - 1]


@pytest.mark.parametrize("args,expected", [
    (2, 3),
    (5, 9),
    (10, 35),
])
def test_solutions(args, expected):
    assert Solution().getKthMagicNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
