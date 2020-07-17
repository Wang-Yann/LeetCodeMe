#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 09:27:54
# @Last Modified : 2020-04-30 09:27:54
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 编写一个算法来判断一个数 n 是不是快乐数。
#
#  「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为 1，那么这个数就是快乐数。
#
#  如果 n 是快乐数就返回 True ；不是，则返回 False 。
#
#
#
#  示例：
#
#  输入：19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
#  Related Topics 哈希表 数学
#  👍 394 👎 0

import pytest


class Solution:
    def isHappy(self, n: int) -> bool:
        def getBitPow(x):
            total_sum = 0
            while x > 0:
                x, digit = divmod(x, 10)
                total_sum += digit ** 2
            return total_sum

        lookup = set()
        while n != 1 and n not in lookup:
            lookup.add(n)
            n = getBitPow(n)
        return n == 1


@pytest.mark.parametrize("args,expected", [
    [19, True],
    [1, True]
])
def test_solutions(args, expected):
    assert Solution().isHappy(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
