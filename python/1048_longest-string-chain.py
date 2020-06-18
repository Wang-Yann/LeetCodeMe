#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一个单词列表，其中每个单词都由小写英文字母组成。 
# 
#  如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac
# " 的前身。 
# 
#  词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_
# 2 是 word_3 的前身，依此类推。 
# 
#  从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。 
#  
# 
#  示例： 
# 
#  输入：["a","b","ba","bca","bda","bdca"]
# 输出：4
# 解释：最长单词链之一为 "a","ba","bda","bdca"。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 16 
#  words[i] 仅由小写英文字母组成。 
#  
# 
#  
#  Related Topics 哈希表 动态规划

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        逆向思维
        """
        words.sort(key=len)
        dp = collections.Counter()
        for word in words:
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1:]
                dp[word] = max(dp[word], dp[new_word] + 1)
        return max(dp.values())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["a", "b", "ba", "bca", "bda", "bdca"], 4)
])
def test_solutions(args, expected):
    assert Solution().longestStrChain(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
