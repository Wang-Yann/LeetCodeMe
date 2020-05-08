#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。 
# 
#  不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。 
# 
#  你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。 
# 
#  
# 
#  示例 1： 
# 
#  输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
#  
# 
#  示例 2： 
# 
#  输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"] 
#  Related Topics 双指针 字符串

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["h", "e"], ["e", "h"]),
    (["h"], ["h"]),
    pytest.param(["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
])
def test_solutions(args, expected):
    Solution().reverseString(args)
    assert args == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
