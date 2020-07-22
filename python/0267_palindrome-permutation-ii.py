#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 17:14:24
# @Last Modified : 2020-07-22 17:14:24
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s ，返回其通过重新排列组合后所有可能的回文字符串，并去除重复的组合。 
# 
#  如不能形成任何回文排列时，则返回一个空列表。 
# 
#  示例 1： 
# 
#  输入: "aabb"
# 输出: ["abba", "baab"] 
# 
#  示例 2： 
# 
#  输入: "abc"
# 输出: [] 
#  Related Topics 回溯算法 
#  👍 28 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = collections.Counter(s)
        mid = [k for k, v in counter.items() if v % 2]
        if len(mid) > 1:
            return []
        mid = '' if mid == [] else mid[0]
        half = ''.join([k * (v // 2) for k, v in counter.items()])
        half = [c for c in half]

        def backtrack(end, path):
            if len(path) == end:
                cur = ''.join(path)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(end):
                    if visited[i] or (i > 0 and half[i] == half[i - 1] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    path.append(half[i])
                    backtrack(end, path)
                    visited[i] = False
                    path.pop()

        ans = []
        N=len(half)
        visited = [False] * N
        backtrack(N, [])
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("aabb", ["abba", "baab"]),
    ("abc", []),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]),
])
def test_solutions(args, expected):
    assert sorted(Solution().generatePalindromes(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
