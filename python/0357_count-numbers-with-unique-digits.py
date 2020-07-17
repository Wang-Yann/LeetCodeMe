#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 23:18:07
# @Last Modified : 2020-05-04 23:18:07
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。
#
#  示例:
#
#  输入: 2
# 输出: 91
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
#
#  Related Topics 数学 动态规划 回溯算法
#  👍 74 👎 0

"""

import pytest


class Solution:

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = [0] * (n + 1)
        dp[1] = 10  # 一位
        dp[2] = 81  # 二位
        sum_cnt = dp[1] + dp[2]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (10 - i + 1)
            sum_cnt += dp[i]
        return sum_cnt


class Solution1(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        count, fk = 10, 9
        for k in range(2, n + 1):
            fk *= 10 - (k - 1)
            count += fk
        return count


@pytest.mark.parametrize("args,expected", [
    (0, 1),
    (2, 91),
    pytest.param(1, 10),
])
def test_solutions(args, expected):
    assert Solution().countNumbersWithUniqueDigits(args) == expected
    assert Solution1().countNumbersWithUniqueDigits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
