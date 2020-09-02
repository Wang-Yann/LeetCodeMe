#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 23:13:38
# @Last Modified : 2020-05-03 23:13:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

#
#
#  注意：本题与主站 65 题相同：https://leetcode-cn.com/problems/valid-number/
#  Related Topics 数学
#  👍 30 👎 0

from enum import Enum

import pytest


class Solution:

    def isNumber(self, s: str) -> bool:
        """
        注意审题 E合法
        书中解法
        """
        s = s.strip()
        self.i = 0
        length = len(s)

        def scan_integer():
            if self.i <= length - 1 and s[self.i] in "+-":
                self.i += 1
            return scan_unsigned_integer()

        def scan_unsigned_integer():
            flag = False
            while self.i <= length - 1 and s[self.i].isdigit():
                self.i += 1
                flag = True
            return flag

        if not s:
            return False
        is_numeric = scan_integer()
        if self.i <= length - 1 and s[self.i] == ".":
            self.i += 1
            is_numeric = scan_unsigned_integer() or is_numeric
        if self.i <= length - 1 and s[self.i] in "eE":
            self.i += 1
            is_numeric = is_numeric and scan_integer()
        return is_numeric and self.i == length


class Solution1:

    def isNumber(self, s: str) -> bool:
        """
        https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/biao-shi-shu-zhi-de-zi-fu-chuan-by-leetcode-soluti/
        """
        ST = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END",
        ])
        CT = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_SPACE",
            "CHAR_ILLEGAL",
        ])

        def toChartype(ch: str) -> CT:
            if ch.isdigit():
                return CT.CHAR_NUMBER
            elif ch.lower() == "e":
                return CT.CHAR_EXP
            elif ch == ".":
                return CT.CHAR_POINT
            elif ch == "+" or ch == "-":
                return CT.CHAR_SIGN
            elif ch == " ":
                return CT.CHAR_SPACE
            else:
                return CT.CHAR_ILLEGAL

        transfer = {
            ST.STATE_INITIAL: {
                CT.CHAR_SPACE: ST.STATE_INITIAL,
                CT.CHAR_NUMBER: ST.STATE_INTEGER,
                CT.CHAR_POINT: ST.STATE_POINT_WITHOUT_INT,
                CT.CHAR_SIGN: ST.STATE_INT_SIGN,
            },
            ST.STATE_INT_SIGN: {
                CT.CHAR_NUMBER: ST.STATE_INTEGER,
                CT.CHAR_POINT: ST.STATE_POINT_WITHOUT_INT,
            },
            ST.STATE_INTEGER: {
                CT.CHAR_NUMBER: ST.STATE_INTEGER,
                CT.CHAR_EXP: ST.STATE_EXP,
                CT.CHAR_POINT: ST.STATE_POINT,
                CT.CHAR_SPACE: ST.STATE_END,
            },
            ST.STATE_POINT: {
                CT.CHAR_NUMBER: ST.STATE_FRACTION,
                CT.CHAR_EXP: ST.STATE_EXP,
                CT.CHAR_SPACE: ST.STATE_END,
            },
            ST.STATE_POINT_WITHOUT_INT: {
                CT.CHAR_NUMBER: ST.STATE_FRACTION,
            },
            ST.STATE_FRACTION: {
                CT.CHAR_NUMBER: ST.STATE_FRACTION,
                CT.CHAR_EXP: ST.STATE_EXP,
                CT.CHAR_SPACE: ST.STATE_END,
            },
            ST.STATE_EXP: {
                CT.CHAR_NUMBER: ST.STATE_EXP_NUMBER,
                CT.CHAR_SIGN: ST.STATE_EXP_SIGN,
            },
            ST.STATE_EXP_SIGN: {
                CT.CHAR_NUMBER: ST.STATE_EXP_NUMBER,
            },
            ST.STATE_EXP_NUMBER: {
                CT.CHAR_NUMBER: ST.STATE_EXP_NUMBER,
                CT.CHAR_SPACE: ST.STATE_END,
            },
            ST.STATE_END: {
                CT.CHAR_SPACE: ST.STATE_END,
            },
        }

        st = ST.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]

        return st in [ST.STATE_INTEGER, ST.STATE_POINT, ST.STATE_FRACTION, ST.STATE_EXP_NUMBER, ST.STATE_END]


@pytest.mark.parametrize("args,expected", [
    ("1.2.3", False),
    ("-123", True),
    ("+1.2", True),
    ("-1E-16", True),
    ("12e+5.4", False),
    ("1 ", True),
    pytest.param("5e2", True),
    pytest.param("+-5", False),
    pytest.param("123e", False),
])
def test_solutions(args, expected):
    assert Solution().isNumber(args) == expected
    assert Solution1().isNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
