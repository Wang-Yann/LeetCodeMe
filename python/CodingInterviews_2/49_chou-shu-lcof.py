#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 22:12:28
# @Last Modified : 2020-04-27 22:12:28
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
#
#
#  示例:
#
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
#  说明:
#
#
#  1 是丑数。
#  n 不超过1690。
#
#
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
#  Related Topics 数学
#  👍 48 👎 0
import pytest


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        dp = [1] + [0] * (n - 1)
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            vp2, vp3, vp5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(vp2, vp3, vp5)
            if dp[i] == vp2:
                p2 += 1
            if dp[i] == vp3:
                p3 += 1
            if dp[i] == vp5:
                p5 += 1
        return dp[n - 1]


@pytest.mark.parametrize("kw,expected", [
    [dict(n=1), 1],
    [dict(n=10), 12],
    [dict(n=12), 16],
])
def test_solutions(kw, expected):
    assert Solution().nthUglyNumber(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
