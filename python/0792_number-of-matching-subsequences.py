#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。 
# 
#  
# 示例:
# 输入: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# 输出: 3
# 解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
#  
# 
#  注意: 
# 
#  
#  所有在words和 S 里的单词都只由小写字母组成。 
#  S 的长度在 [1, 50000]。 
#  words 的长度在 [1, 5000]。 
#  words[i]的长度在[1, 50]。 
#  
#  Related Topics 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        ans = 0
        heads = collections.defaultdict(list)
        for word in words:
            it = iter(word)
            heads[next(it)].append(it)
        for letter in S:
            old_bucket = heads[letter]
            heads[letter] = []
            while old_bucket:
                it = old_bucket.pop()
                nex = next(it, None)
                if nex:
                    heads[nex].append(it)
                else:
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        waiting = collections.defaultdict(list)
        for word in words:
            it = iter(word)
            waiting[next(it, None)].append(it)
        # print(waiting)
        for char in S:
            for it in waiting.pop(char, ()):
                waiting[next(it, None)].append(it)
        # print(waiting)
        return len(waiting[None])


@pytest.mark.parametrize("kwargs,expected", [
    (dict(S="abcde", words=["a", "bb", "acd", "ace"]), 3),
    (dict(S="dcaog", words = ['dog', 'cat', 'cop']), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().numMatchingSubseq(**kwargs) == expected
    assert Solution1().numMatchingSubseq(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
