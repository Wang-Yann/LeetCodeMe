#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-28 22:43:30
# @Last Modified : 2020-04-28 22:43:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 编写一个程序，找出第 n 个丑数。
#
#  丑数就是质因数只包含 2, 3, 5 的正整数。
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
#  Related Topics 堆 数学 动态规划
#  👍 328 👎 0

"""



import pytest


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        dp = [1] + [0] * (n - 1)
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            vp2, vp3, vp5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(vp2, vp3, vp5)
            if vp2 == dp[i]:
                p2 += 1
            if vp3 == dp[i]:
                p3 += 1
            if vp5 == dp[i]:
                p5 += 1
        return dp[n - 1]


sol = Solution()


@pytest.mark.parametrize("args,expected", [
    (1, 1),
    pytest.param(10, 12),
])
def test_solutions(args, expected):
    assert sol.nthUglyNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "-v", "--color=yes", __file__])
