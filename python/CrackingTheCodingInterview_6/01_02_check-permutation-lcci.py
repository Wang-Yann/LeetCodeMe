#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:26:18
# @Last Modified : 2020-07-11 23:26:18
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。 
# 
#  示例 1： 
# 
#  输入: s1 = "abc", s2 = "bca"
# 输出: true 
#  
# 
#  示例 2： 
# 
#  输入: s1 = "abc", s2 = "bad"
# 输出: false
#  
# 
#  说明： 
# 
#  
#  0 <= len(s1) <= 100 
#  0 <= len(s2) <= 100 
#  
#  Related Topics 数组 字符串 
#  👍 12 👎 0


"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return collections.Counter(s1) == collections.Counter(s2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s1="abc", s2="bca"), True],

    pytest.param(dict(s1="abc", s2="bad"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().CheckPermutation(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
