#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例: 
# 
#  输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#  
# 
#  
# 
#  提示： 
# 
#  
#  该字符串只包含小写英文字母。 
#  给定字符串的长度和 k 在 [1, 10000] 范围内。 
#  
#  Related Topics 字符串

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length =len(s)
        ans =""
        for i in range(0,length,2*k):
            ans+=s[i:i+k][::-1]+s[i+k:i+2*k]
        return ans



# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kwargs,expected", [
    (dict(s = "abcdefg", k = 2), "bacdfeg"),
    (dict(s = "abcdefgh", k = 3), "cbadefhg"),
])
def test_solutions(kwargs, expected):
    assert Solution().reverseStr(**kwargs) == expected








if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

