#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。 
# 
#  说明： 
# 
#  
#  拆分时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#  
# 
#  示例 2： 
# 
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#  
#  Related Topics 动态规划

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    """  dp[i]表示s的前i位是否可以用 wordDict中的单词表示。"""

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @functools.lru_cache(None)
        def back_track(ss):
            if not ss:
                return True
            res = False
            for i in range(1, len(ss) + 1):
                if ss[:i] in wordDict:
                    res = back_track(ss[i:]) or res
            return res

        return back_track(s)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="leetcode", wordDict=["leet", "code"]), True),
    (dict(s="applepenapple", wordDict=["apple", "pen"]), True),
    (dict(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]), False),
])
def test_solutions(kwargs, expected):
    assert Solution().wordBreak(**kwargs) == expected
    assert Solution1().wordBreak(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
