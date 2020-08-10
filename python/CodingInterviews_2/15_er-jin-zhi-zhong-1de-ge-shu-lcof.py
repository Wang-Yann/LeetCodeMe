#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 23:51:06
# @Last Modified : 2020-04-25 23:51:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出
# 2。
#
#  示例 1：
#
#  输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
#
#
#  示例 2：
#
#  输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
#
#
#  示例 3：
#
#  输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
#
#
#
#  注意：本题与主站 191 题相同：https://leetcode-cn.com/problems/number-of-1-bits/
#  Related Topics 位运算
#  👍 35 👎 0
import pytest


class Solution0:

    def hammingWeight(self, n: int) -> int:
        e = 0b1
        ans = 0
        for i in range(32):
            if e & n != 0b0:
                ans += 1
            e <<= 1
        return ans


class Solution:

    def hammingWeight(self, n: int) -> int:
        """对于任意数字 n ，将 n 和 n - 1做与运算，会把最后一个 1的位变成 0"""
        ans = 0
        while n != 0b0:
            ans += 1
            n &= (n - 0b1)
        return ans


@pytest.mark.parametrize("args,expected", [
    [0b00000000000000000000000000001011, 3],
    [0b00000000000000000000000010000000, 1],
    [0b11111111111111111111111111111101, 31],
])
def test_solutions(args, expected):
    assert Solution().hammingWeight(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
