#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:06:38
# @Last Modified : 2020-07-13 14:06:38
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。 
# 
#  注意：本题相对原题稍作修改 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 4 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = collections.defaultdict(list)
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(strs=["eat", "tea", "tan", "ate", "nat", "bat"]),
     [
         ["ate", "eat", "tea"],
         ["nat", "tan"],
         ["bat"]
     ]
     ],
])
def test_solutions(kw, expected):
    res = Solution().groupAnagrams(**kw)
    res.sort(key=len, reverse=True)
    assert len(res) == len(expected)
    for i in range(len(res)):
        assert sorted(res[i]) == sorted(expected[i])


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
