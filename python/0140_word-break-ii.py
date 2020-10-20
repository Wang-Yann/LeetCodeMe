#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的
# 句子。 
# 
#  说明： 
# 
#  
#  分隔时可以重复使用字典中的单词。 
#  你可以假设字典中没有重复的单词。 
#  
# 
#  示例 1： 
# 
#  输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
#  
# 
#  示例 2： 
# 
#  输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
#  
#  Related Topics 动态规划 回溯算法

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        记忆化DFS
        """

        @functools.lru_cache(None)
        def dfs(cur):
            if cur == '':
                return []
            res = []
            for word in wordDict:
                if not cur.startswith(word):
                    continue
                # 循环到最后而且匹配，则append
                if len(word) == len(cur):
                    res.append(word)
                # 匹配但是没有循环到最后，于是继续往下，之后需要对返回的结果分别加上当前的word
                else:
                    rest = dfs(cur[len(word):])
                    for item in rest:
                        item = word + ' ' + item
                        res.append(item)
            # 保存当前s的结果
            return res

        return dfs(s)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """
    HARD HARD HARD
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(start, path):
            if start == length:
                result.append(" ".join(path))
                return
            for i in range(start, length):
                if valid[start][i]:
                    path += [s[start:i + 1]]
                    dfs(i + 1, path)
                    path.pop()

        length = len(s)
        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))
        can_break = [False for _ in range(length + 1)]
        valid = [[False] * length for _ in range(length)]
        can_break[0] = True
        for i in range(1, length + 1):
            for l in range(1, min(i, max_len) + 1):
                if can_break[i - l] and s[i - l:i] in wordDict:
                    valid[i - l][i - 1] = True
                    can_break[i] = True

        result = []
        if can_break[-1]:
            dfs(0, [])
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(
        s="catsanddog",
        wordDict=["cat", "cats", "and", "sand", "dog"]
    ),
        ["cats and dog", "cat sand dog"]
    ],
    [dict(
        s="pineapplepenapple",
        wordDict=["apple", "pen", "applepen", "pine", "pineapple"]
    ), [
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple"
    ]
    ],
    [dict(
        s="catsandog",
        wordDict=["cats", "dog", "sand", "and", "cat"]
    ),
        []
    ],
])
def test_solutions(kw, expected):
    assert sorted(Solution().wordBreak(**kw)) == sorted(expected)
    assert sorted(Solution1().wordBreak(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
