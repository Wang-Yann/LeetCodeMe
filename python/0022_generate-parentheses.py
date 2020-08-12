#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-09 20:41:04
# @Last Modified : 2020-04-09 20:41:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
"""
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法
#  👍 1170 👎 0

"""

from typing import List

import pytest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []

        def helper(current, left, right):
            if left == 0 and right == 0:
                res.append(current)
            if left > 0:
                helper(current + "(", left - 1, right)
            if left < right:
                helper(current + ")", left, right - 1)

        res = []
        helper("", n, n)
        return res


class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        """Me"""
        if n <= 0:
            return []
        res = []

        def dfs(path, ln, rn):
            if ln > rn or ln < 0 or rn < 0:
                return
            elif ln < rn:
                dfs(path + ")", ln, rn - 1)
                dfs(path + "(", ln - 1, rn)
            else:
                if ln == rn == 0:
                    res.append(path[:])
                else:
                    dfs(path + "(", ln - 1, rn)

        dfs("", n, n)
        return list(res)


@pytest.mark.parametrize("CLS", [
    Solution, Solution1
])
@pytest.mark.parametrize("kw,expected", [
    (dict(n=4),
     ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()',
      '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
     ),
])
def test_solutions(kw, expected, CLS):
    assert sorted(CLS().generateParenthesis(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
