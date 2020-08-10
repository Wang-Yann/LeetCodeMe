#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-09 21:19:46
# @Last Modified : 2020-04-09 21:19:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#  示例:
#
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
#  说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#  Related Topics 字符串 回溯算法
#  👍 796 👎 0

"""
from typing import List

import pytest


class Solution:
    character_list = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = set()
        visit_set = set()
        self.dfs(digits, res, "", 0, len(digits), visit_set)
        return list(res)

    def dfs(self, digits, res, current, idx, l, visit_set):
        if idx == l:
            res.add(current)
        elif idx > l:
            return
        else:
            for c in self.character_list[digits[idx]]:
                if (idx + 1, c, current) not in visit_set:
                    self.dfs(digits, res, current + c, idx + 1, l, visit_set)
                    visit_set.add((idx + 1, c, current))


class Solution1(object):
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
        N = len(digits)

        def dfs(cur, n):
            if n == N:
                result.append(cur)
                return
            for choice in lookup[int(digits[n])]:
                dfs(cur + choice, n + 1)

        dfs("", 0)
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(digits="23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().letterCombinations(**kw)) == sorted(expected)
    assert sorted(Solution1().letterCombinations(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
