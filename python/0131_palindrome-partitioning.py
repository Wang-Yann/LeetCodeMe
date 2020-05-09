#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。 
# 
#  返回 s 所有可能的分割方案。 
# 
#  示例: 
# 
#  输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ] 
#  Related Topics 回溯算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(cur, i):
            if i == length:
                result.append(list(cur))
            else:
                for j in range(i, length):
                    if isPalindrome(s[i:j + 1]):
                        cur.append(s[i:j + 1])
                        dfs(cur, j + 1)
                        cur.pop()

        def isPalindrome(Str):
            for i in range(len(Str) // 2):
                if Str[i] != Str[-(i + 1)]:
                    return False
            return True

        result = []
        length = len(s)
        dfs([], 0)
        return result


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("aab", [["aa", "b"], ["a", "a", "b"]])
])
def test_solutions(args, expected):
    res = Solution().partition(args)
    assert sorted([sorted(x) for x in res]) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
