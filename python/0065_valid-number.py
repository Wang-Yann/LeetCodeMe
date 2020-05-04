#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 23:13:38
# @Last Modified : 2020-05-03 23:13:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution0:

    def isNumber(self, s: str) -> bool:
        """注意审题 E不合法"""
        s=s.strip()
        self.i = 0
        length = len(s)

        def scan_integer():
            if self.i<=length-1 and s[self.i] in "+-":
                self.i += 1
            return scan_unsigned_integer()

        def scan_unsigned_integer():
            flag=False
            while self.i <= length-1  and s[self.i].isdigit():
                self.i += 1
                flag=True
            return flag
        if not s:
            return False
        is_numeric = scan_integer()
        if self.i<=length-1 and s[self.i] == ".":
            self.i += 1
            is_numeric = scan_unsigned_integer() or is_numeric
        if self.i<=length-1 and s[self.i] in "e":
            self.i += 1
            is_numeric = is_numeric and scan_integer()
        return is_numeric and self.i == length


class InputType(object):
    INVALID=0
    SPACE=1
    SIGN=2
    DIGIT=3
    DOT=4
    EXPONENT=5


class Solution:

    def isNumber(self, s: str) -> bool:
        """DFA
        http://images.cnitblog.com/i/627993/201405/012016243309923.png
        https://leetcode-cn.com/problems/valid-number/solution/biao-qu-dong-fa-by-user8973/
        """
        transition_table = [[-1,  0,  3,  1,  2, -1],     # next states for state 0
                            [-1,  8, -1,  1,  4,  5],     # next states for state 1
                            [-1, -1, -1,  4, -1, -1],     # next states for state 2
                            [-1, -1, -1,  1,  2, -1],     # next states for state 3
                            [-1,  8, -1,  4, -1,  5],     # next states for state 4
                            [-1, -1,  6,  7, -1, -1],     # next states for state 5
                            [-1, -1, -1,  7, -1, -1],     # next states for state 6
                            [-1,  8, -1,  7, -1, -1],     # next states for state 7
                            [-1,  8, -1, -1, -1, -1]]     # next states for state 8

        state = 0
        for char in s:
            input_type= InputType.INVALID
            if char.isspace():
                input_type = InputType.SPACE
            elif char in "+-":
                input_type = InputType.SIGN
            elif char.isdigit():
                input_type =InputType.DIGIT
            elif char==".":
                input_type = InputType.DOT
            elif char=="e":
                input_type=InputType.EXPONENT
            state = transition_table[state][input_type]
            if state==-1:
                return False
        return state in (1,4,7,8)




@pytest.mark.parametrize("args,expected", [
    ("1.2.3", False),
    ("-123", True),
    ("+1.2", True),
    ("-1E-16", False),
    ("12e+5.4", False),
    ("1 ", True),
    pytest.param("5e2", True),
    pytest.param("+-5", False),
    pytest.param("123e", False),
])
def test_solutions(args, expected):
    assert Solution0().isNumber(args) == expected
    assert Solution().isNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
