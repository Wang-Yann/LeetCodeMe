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
        res = []
        self.helper(res, "", n, n)
        return list(res)

    def helper(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.helper(result, current + "(", left - 1, right)
        if left < right:
            self.helper(result, current + ")", left, right - 1)


class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        res = set()
        # self.dfs(res_set,"",n,n)
        self.dfs(res, "", n, n)
        return list(res)

    def dfs(self, res_set, path, ln, rn):
        if ln > rn or ln < 0 or rn < 0:
            return
        elif ln < rn:
            self.dfs(res_set, path + ")", ln, rn - 1)
            self.dfs(res_set, path + "(", ln - 1, rn)
        else:
            if ln == rn == 0:
                res_set.add(path)
            else:
                self.dfs(res_set, path + "(", ln - 1, rn)


@pytest.mark.parametrize("CLS", [
    Solution, Solution1
])
@pytest.mark.parametrize("kw,expected", [
    [dict(n=4),
     ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()',
      '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
     ],
])
def test_solutions(kw, expected, CLS):
    assert sorted(CLS().generateParenthesis(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
