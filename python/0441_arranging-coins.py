#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 17:27:09
# @Last Modified : 2020-04-30 17:27:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
#
#  给定一个数字 n，找出可形成完整阶梯行的总行数。
#
#  n 是一个非负整数，并且在32位有符号整型的范围内。
#
#  示例 1:
#
#
# n = 5
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤
#
# 因为第三行不完整，所以返回2.
#
#
#  示例 2:
#
#
# n = 8
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# 因为第四行不完整，所以返回3.
#
#  Related Topics 数学 二分查找
#  👍 63 👎 0

"""

import pytest


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n in (0, 1):
            return n
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            v = (1 + mid) * mid // 2
            if v < n:
                l = mid + 1
            elif v > n:
                r = mid - 1
            else:
                return mid
        return l-1


@pytest.mark.parametrize("args,expected", [
    (5, 2),
    (8, 3)
])
def test_solutions(args, expected):
    assert Solution().arrangeCoins(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
