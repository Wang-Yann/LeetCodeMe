#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans =""
        for chars in zip(*strs):
            if all( x==chars[0] for x in chars):
                ans+=chars[0]
            else:
                return ans
        return ans

# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        strs.sort(key=len )
        ans =""
        for i,char in enumerate(strs[0]):
            if all( x[i]==char for x in strs):
                ans+=char
            else:
                return ans
        return ans

@pytest.mark.parametrize("args,expected", [
    (["flower","flow","flight"], "fl"),
    pytest.param(["dog","racecar","car"], ""),
])
def test_solutions(args, expected):
    assert Solution().longestCommonPrefix(args) == expected
    assert Solution1().longestCommonPrefix(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])