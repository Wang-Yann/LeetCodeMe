#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有台奇怪的打印机有以下两个特殊要求： 
# 
#  
#  打印机每次只能打印同一个字符序列。 
#  每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。 
#  
# 
#  给定一个只包含小写英文字母的字符串，你的任务是计算这个打印机打印它需要的最少次数。 
# 
#  示例 1: 
# 
#  
# 输入: "aaabbb"
# 输出: 2
# 解释: 首先打印 "aaa" 然后打印 "bbb"。
#  
# 
#  示例 2: 
# 
#  
# 输入: "aba"
# 输出: 2
# 解释: 首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。 
# 
#  提示: 输入字符串的长度不会超过 100。 
#  Related Topics 深度优先搜索 动态规划

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        https://leetcode-cn.com/problems/strange-printer/solution/qi-guai-de-da-yin-ji-by-leetcode/
        """
        memo = {}
        def dfs(i,j):
            if i>j:
                return 0
            if (i,j) not in memo:
                ans =dfs(i+1,j)+1
                for k in range(i+1,j+1):
                    if s[k]==s[i]:
                        ans = min(ans,dfs(i,k-1)+dfs(k+1,j))
                memo[(i,j)]=ans
            return memo[(i,j)]
        return dfs(0,len(s)-1)
        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("aaabbb", 2),
    pytest.param("aba", 2),
])
def test_solutions(args, expected):
    assert Solution().strangePrinter(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])