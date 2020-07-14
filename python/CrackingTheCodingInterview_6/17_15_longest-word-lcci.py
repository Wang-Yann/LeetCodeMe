#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 22:06:55
# @Last Modified : 2020-07-14 22:06:55
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符
# 合要求的单词则返回空字符串。 
#  示例： 
#  输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
# 输出： "dogwalker"
# 解释： "dogwalker"可由"dog"和"walker"组成。
#  
#  提示： 
#  
#  0 <= len(words) <= 100 
#  1 <= len(words[i]) <= 100 
#  
#  Related Topics 字符串 
#  👍 6 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestWord(self, words: List[str]) -> str:
        d = set(words)
        words.sort(key=lambda x:(-len(x), x))

        def dfs(word, k):
            if word in d and k:
                return True
            for i in range(len(word)):
                if word[:i] in d and dfs(word[i:], k + 1):
                    return True
            return False

        for word in words:
            if dfs(word, 0):
                return word
        return ""


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(words=["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]), "dogwalker"],

])
def test_solutions(kwargs, expected):
    assert Solution().longestWord(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
