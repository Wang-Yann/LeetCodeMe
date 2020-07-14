#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 21:34:59
# @Last Modified : 2020-07-14 21:34:59
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，
# 你能对此优化吗? 
# 
#  示例： 
# 
#  输入：words = ["I","am","a","student","from","a","university","in","a","city"], 
# word1 = "a", word2 = "student"
# 输出：1 
# 
#  提示： 
# 
#  
#  words.length <= 100000 
#  
#  Related Topics 双指针 字符串 
#  👍 10 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = float("-inf"), float("inf")
        res = len(words)
        for idx, word in enumerate(words):
            if word == word1:
                idx1 = idx
            elif word == word2:
                idx2 = idx
            res = min(res, abs(idx1 - idx2))
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(words=["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"],
          word1="a", word2="student"), 1],

])
def test_solutions(kwargs, expected):
    assert Solution().findClosest(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
