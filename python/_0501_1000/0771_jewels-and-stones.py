#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。 
# 
#  J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。 
# 
#  示例 1: 
# 
#  输入: J = "aA", S = "aAAbbbb"
# 输出: 3
#  
# 
#  示例 2: 
# 
#  输入: J = "z", S = "ZZ"
# 输出: 0
#  
# 
#  注意: 
# 
#  
#  S 和 J 最多含有50个字母。 
#  J 中的字符不重复。 
#  
#  Related Topics 哈希表

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        lookup = set(J)
        return sum(char in lookup for char in S)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(J="aA", S="aAAbbbb"), 3],
    [dict(J="z", S="ZZ"), 0],
])
def test_solutions(kw, expected):
    assert Solution().numJewelsInStones(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
