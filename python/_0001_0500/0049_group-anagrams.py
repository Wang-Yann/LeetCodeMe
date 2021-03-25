#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
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

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =collections.defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())




# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["eat", "tea", "tan", "ate", "nat", "bat"],
     [["ate","eat","tea"], ["nat","tan"], ["bat"]] )
])
def test_solutions(args, expected):
    res =  Solution().groupAnagrams(args)
    assert sorted([sorted(x) for x in res]) ==sorted([sorted(x) for x in expected])




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])