#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:49:46
# @Last Modified : 2020-07-11 23:49:46
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。 
# 
#  回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。 
# 
#  回文串不一定是字典当中的单词。 
# 
#  
# 
#  示例1： 
# 
#  输入："tactcoa"
# 输出：true（排列有"tacocat"、"atcocta"，等等）
#  
# 
#  
#  Related Topics 哈希表 字符串 
#  👍 26 👎 0


"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        return sum(v % 2 for v in counter.values()) <= 1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ["tactcoa", True],
])
def test_solutions(args, expected):
    assert Solution().canPermutePalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
