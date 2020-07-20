#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:03:17
# @Last Modified : 2020-05-10 18:03:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
#
#  例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
#
#
#
#  示例 1：
#
#  输入：n = 12
# 输出：5
#
#
#  示例 2：
#
#  输入：n = 13
# 输出：6
#
#
#
#  限制：
#
#
#  1 <= n < 2^31
#
#
#  注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/
#  Related Topics 数学
#  👍 57 👎 0

import functools

import pytest


class Solution:

    def countDigitOne(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n):
            if n <= 0:
                return 0
            num_str = str(n)
            high = int(num_str[0])
            pow_base = 10 ** (len(num_str) - 1)
            last = n - high * pow_base
            if high == 1:
                # // 最高位是1，如1234, 此时pow = 1000,那么结果由以下三部分构成：
                # // (1) dfs(pow - 1)代表[0,999]中1的个数;
                # // (2) dfs(last)代表234中1出现的个数;
                # // (3) last+1代表固定高位1有多少种情况。

                return dfs(pow_base - 1) + dfs(last) + last + 1
            else:
                # // 最高位不为1，如2234，那么结果也分成以下三部分构成：
                # // (1) pow代表固定高位1，有多少种情况;
                # // (2) high * dfs(pow - 1)代表999以内和1999以内低三位1出现的个数;
                # // (3) dfs(last)同上。

                return pow_base + high * dfs(pow_base - 1) + dfs(last)

        return dfs(n)


@pytest.mark.parametrize("args,expected", [
    (12, 5),
    pytest.param(13, 6),
])
def test_solutions(args, expected):
    assert Solution().countDigitOne(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
