#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 18:13:58
# @Last Modified : 2020-07-21 18:13:58
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。 
# 
#  示例: 
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"] 
# 
#  输入: word1 = “coding”, word2 = “practice”
# 输出: 3
#  
# 
#  输入: word1 = "makes", word2 = "coding"
# 输出: 1
#  
# 
#  注意: 
# 你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。 
#  Related Topics 数组 
#  👍 22 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        lookup = collections.defaultdict(list)
        for i, word in enumerate(words):
            lookup[word].append(i)
        dis1 = lookup[word1]
        dis2 = lookup[word2]
        return min(abs(a - b) for a in dis1 for b in dis2)

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(word1="coding", word2="practice"), 3],
    [dict(word1="makes", word2="coding"), 1],
])
@pytest.mark.parametrize("words", (["practice", "makes", "perfect", "coding", "makes"],))
def test_solutions(kw, expected, words):
    kw["words"] = words
    assert Solution().shortestDistance(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
