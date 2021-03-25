#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-30 22:32:41
# @Last Modified : 2020-04-30 22:32:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。
#
#  以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。
#
#
#
#  示例 1：
#
#
# 输入："13"
# 输出："3"
# 解释：13 的 3 进制是 111。
#
#
#  示例 2：
#
#
# 输入："4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
#
#
#  示例 3：
#
#
# 输入："1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。
#
#
#
#
#  提示：
#
#
#  n的取值范围是 [3, 10^18]。
#  输入总是有效且没有前导 0。
#
#
#
#  Related Topics 数学 二分查找
#  👍 35 👎 0

"""
import math

import pytest


class Solution:

    def smallestGoodBase(self, n: str) -> str:
        """
        看不懂
        TODO
        """
        num = int(n)
        max_len = int(math.log(num, 2))
        for l in range(max_len, 1, -1):
            b = int(num ** (l ** (-1)))
            if (b ** (l + 1) - 1) // (b - 1) == num:
                return str(b)
        return str(num - 1)



@pytest.mark.parametrize("args,expected", [
    ("13", "3"),
    pytest.param("4681", "8"),
    pytest.param("1000000000000000000", "999999999999999999"),
])
def test_solutions(args, expected):
    assert Solution().smallestGoodBase(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
