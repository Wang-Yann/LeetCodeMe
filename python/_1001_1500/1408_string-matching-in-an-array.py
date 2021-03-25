#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。 
# 
#  如果你可以删除 words[j] 最左侧和/或最右侧的若干字符得到 word[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串
# 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：words = ["mass","as","hero","superhero"]
# 输出：["as","hero"]
# 解释："as" 是 "mass" 的子字符串，"hero" 是 "superhero" 的子字符串。
# ["hero","as"] 也是有效的答案。
#  
# 
#  示例 2： 
# 
#  输入：words = ["leetcode","et","code"]
# 输出：["et","code"]
# 解释："et" 和 "code" 都是 "leetcode" 的子字符串。
#  
# 
#  示例 3： 
# 
#  输入：words = ["blue","green","bu"]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 30 
#  words[i] 仅包含小写英文字母。 
#  题目数据 保证 每个 words[i] 都是独一无二的。 
#  
#  Related Topics 字符串

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        暴力解的结果
        Success: Runtime:40 ms, faster than 91.38% of Python3 online submissions. Memory Usage:13.8 MB,
        less than 100.00% of Python3 online submissions.
        """
        N = len(words)
        words_set = sorted(words, key=len)
        ans = []
        for i, word in enumerate(words_set):
            for j in range(N - 1, i, -1):
                if word in words_set[j]:
                    ans.append(word)
                    break
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Suffix Tree
        执行用时： 60 ms , 在所有 Python3 提交中击败了 23.08% 的用户 内存消耗： 14.4 MB ,
         在所有 Python3 提交中击败了 100.00% 的用户
        """

        def add(word: str):
            node = trie
            for c in word:
                node = node.setdefault(c, {})

        def get(word: str) -> bool:
            node = trie
            for c in word:
                node = node.get(c)
                if node is None:
                    return False
            return True

        words.sort(key=len, reverse=True)
        trie, result = {}, []
        for word in words:
            if get(word):
                result.append(word)
            for i in range(len(word)):
                add(word[i:])
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(words=["mass", "as", "hero", "superhero"]), ["as", "hero"]],
    [dict(words=["leetcode", "et", "code"]), ["et", "code"]],
    [dict(words=["blue", "green", "bu"]), []],
])
def test_solutions(kw, expected):
    assert Solution().stringMatching(**kw) == expected
    assert set(Solution1().stringMatching(**kw)) == set(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
