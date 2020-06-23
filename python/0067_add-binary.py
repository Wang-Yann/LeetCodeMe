#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20

"""
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
#  输入为 非空 字符串且只包含数字 1 和 0。
#
#
#
#  示例 1:
#
#  输入: a = "11", b = "1"
# 输出: "100"
#
#  示例 2:
#
#  输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
#
#  提示：
#
#
#  每个字符串仅由字符 '0' 或 '1' 组成。
#  1 <= a.length, b.length <= 10^4
#  字符串如果不是 "0" ，就都不含前导零。
#
#  Related Topics 数学 字符串

"""
import pytest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena, lenb = len(a), len(b)
        if lena < lenb:
            a = "0" * (lenb - lena) + a
        else:
            b = "0" * (lena - lenb) + b
        res = ""
        carry = 0
        i = max(lena, lenb) - 1
        while i >= 0:
            v_sum = int(a[i]) + int(b[i]) + carry
            carry = v_sum // 2
            res = str(v_sum % 2) + res
            i -= 1
        if carry:
            res = "1" + res
        return res


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        """x 保存结果,y 保存进位"""
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]


@pytest.mark.parametrize("kw,expected", [
    [dict(a="11", b="1"), "100"],
    [dict(a="1010", b="1011"), "10101"],
])
def test_solutions(kw, expected):
    assert Solution().addBinary(**kw) == expected
    assert Solution1().addBinary(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
