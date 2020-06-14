#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 你有一个单词列表 words 和一个模式 pattern，你想知道 words 中的哪些单词与模式匹配。 
# 
#  如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。 
# 
#  （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。） 
# 
#  返回 words 中与给定模式匹配的单词列表。 
# 
#  你可以按任何顺序返回答案。 
# 
#  
# 
#  示例： 
# 
#  输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# 输出：["mee","aqq"]
# 解释：
# "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
# "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
# 因为 a 和 b 映射到同一个字母。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 50 
#  1 <= pattern.length = words[i].length <= 20 
#  
#  Related Topics 字符串

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            lookup = {}
            for p, w in zip(pattern, word):
                if lookup.setdefault(p, w) != w:
                    return False
            return len(set(lookup.values())) == len(lookup.values())

        return list(filter(match, words))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def is_mapped(word):
            if len(word) != LEN_P:
                return False
            lookup_p, lookup_w = {}, {}
            for char_w, char_p in zip(word, pattern):
                if char_w not in lookup_w and char_p not in lookup_p:
                    lookup_w[char_w] = char_p
                    lookup_p[char_p] = char_w
                elif lookup_p.get(char_p) != char_w or lookup_w.get(char_w) != char_p:
                    return False
            return True

        LEN_P = len(pattern)
        return list(filter(is_mapped, words))


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"
    ), ["mee", "aqq"]),
])
def test_solutions(kwargs, expected):
    assert Solution().findAndReplacePattern(**kwargs) == expected
    assert Solution1().findAndReplacePattern(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
