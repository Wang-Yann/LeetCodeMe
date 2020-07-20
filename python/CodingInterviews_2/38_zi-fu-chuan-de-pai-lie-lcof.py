#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 17:10:27
# @Last Modified : 2020-05-10 17:10:27
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#
#
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#
#
#  示例:
#
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#
#
#
#
#  限制：
#
#  1 <= s 的长度 <= 8
#  Related Topics 回溯算法
#  👍 59 👎 0

from typing import List

import pytest


class Solution:

    def permutation(self, s: str) -> List[str]:

        res = [""]
        chars_list = list(s)
        for char in chars_list:
            next_level = []
            for now_word in res:
                for i in range(len(now_word) + 1):
                    candidate = now_word[:i] + char + now_word[i:]
                    if candidate not in next_level:
                        next_level.append(candidate)
            res = next_level
        return res


class Solution1:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c)) # 添加排列方案
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i] # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1) # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i] # 恢复交换
        dfs(0)
        return res



class SolutionMe:
    def permutation(self, s: str) -> List[str]:
        """GOOD"""
        def dfs(begin):
            if begin==length:
                res.append("".join(chars_list))
            dic=set()
            for i in range(begin,length):
                if chars_list[i] in dic:continue
                dic.add(chars_list[i])
                chars_list[begin],chars_list[i]=chars_list[i],chars_list[begin]
                dfs(begin+1)
                chars_list[begin],chars_list[i]=chars_list[i],chars_list[begin]
        res =[]
        length=len(s)
        chars_list=list(s)
        dfs(0)
        return res


@pytest.mark.parametrize("args,expected", [
    ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
    ("aab", ["aba", "aab", "baa"]),
])
def test_solutions(args, expected):
    assert sorted(Solution().permutation(args)) == sorted(expected)
    assert sorted(Solution1().permutation(args)) == sorted(expected)
    assert sorted(SolutionMe().permutation(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
