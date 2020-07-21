#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 18:26:40
# @Last Modified : 2020-07-21 18:26:40
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。 
# 
#  word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。 
# 
#  示例: 
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"]. 
# 
#  输入: word1 = “makes”, word2 = “coding”
# 输出: 1
#  
# 
#  输入: word1 = "makes", word2 = "makes"
# 输出: 3
#  
# 
#  注意: 
# 你可以假设 word1 和 word2 都在列表里。 
#  Related Topics 数组 
#  👍 15 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        dist = float("inf")
        is_same = (word1 == word2)
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                if is_same and index1 is not None:
                    dist = min(dist, abs(index1 - i))
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1

        return dist


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(word1="makes", word2="coding"), 1],
    [dict(word1="makes", word2="makes"), 3],
])
@pytest.mark.parametrize("words", (["practice", "makes", "perfect", "coding", "makes"],))
def test_solutions(kw, expected, words):
    kw["words"] = words
    assert Solution().shortestWordDistance(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
