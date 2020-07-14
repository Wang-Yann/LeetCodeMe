#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 22:36:42
# @Last Modified : 2020-07-14 22:36:42
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字
# 符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。 
# 
#  示例： 
# 
#  输入：
# big = "mississippi"
# smalls = ["is","ppi","hi","sis","i","ssippi"]
# 输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
#  
# 
#  提示： 
# 
#  
#  0 <= len(big) <= 1000 
#  0 <= len(smalls[i]) <= 1000 
#  smalls的总字符数不会超过 100000。 
#  你可以认为smalls中没有重复字符串。 
#  所有出现的字符均为英文小写字母。 
#  
#  Related Topics 字典树 字符串 
#  👍 6 👎 0


"""

import collections
from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
trie = lambda:collections.defaultdict(trie)


class Solution:

    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        """
        AC  好无聊的题目
        """
        Trie = trie()
        for i, word in enumerate(smalls):
            cur = Trie
            for char in word:
                cur = cur[char]
            cur["_end"] = word
        N = len(smalls)
        smalls_map = {word:i for i, word in enumerate(smalls)}
        ans = [[] for _ in range(N)]
        for i in range(len(big)):
            cur = Trie
            searched_words = set()
            for char in big[i:]:
                if char not in cur:
                    break
                if cur[char]["_end"]:
                    searched_words.add(cur[char]["_end"])
                cur = cur[char]
            for w in searched_words:
                ans[smalls_map[w]].append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        big="mississippi",
        smalls=["is", "ppi", "hi", "sis", "i", "ssippi"]
    ), [[1, 4], [8], [], [3], [1, 4, 7, 10], [5]]],

])
def test_solutions(kwargs, expected):
    assert Solution().multiSearch(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
