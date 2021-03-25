#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。 
# 
#  例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0,
#  2, 5]。 
# 
#  对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。 
# 
#  那么成功对给定单词列表进行编码的最小字符串长度是多少呢？ 
# 
#  
# 
#  示例： 
# 
#  输入: words = ["time", "me", "bell"]
# 输出: 10
# 说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 2000 
#  1 <= words[i].length <= 7 
#  每个单词都是小写字母 。 
#  
# 

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)


# leetcode submit region end(Prohibit modification and deletion)
Trie = lambda:collections.defaultdict(Trie)


class Solution1:

    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        trie = Trie()

        nodes = []
        # print([functools.reduce(dict.__getitem__, word[::-1], trie)
        #       for word in words])
        for word in words:
            cur = trie
            for char in reversed(word):
                cur = cur[char]
            nodes.append(cur)
        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)


@pytest.mark.parametrize("args,expected", [
    (["time", "me", "bell"], 10),
])
def test_solutions(args, expected):
    # assert Solution().minimumLengthEncoding(args) == expected
    assert Solution1().minimumLengthEncoding(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
