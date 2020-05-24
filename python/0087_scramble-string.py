#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。 
# 
#  下图是字符串 s1 = "great" 的一种可能的表示形式。 
# 
#      great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
#  
# 
#  在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。 
# 
#  例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。 
# 
#      rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
#  
# 
#  我们将 "rgeat” 称作 "great" 的一个扰乱字符串。 
# 
#  同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。 
# 
#      rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
#  
# 
#  我们将 "rgtae” 称作 "great" 的一个扰乱字符串。 
# 
#  给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。 
# 
#  示例 1: 
# 
#  输入: s1 = "great", s2 = "rgeat"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s1 = "abcde", s2 = "caebd"
# 输出: false 
#  Related Topics 字符串 动态规划

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """https://www.jiuzhang.com/solution/scramble-string#tag-highlight-lang-python
        第k个字符后分割
        """
        n = len(s1)
        dp = [[[False]*(n+1) for _ in range(n) ] for _ in  range(n)]
        for i in range(n):
            for j in range(n):
                if s1[i]==s2[j]:
                    dp[i][j][1]=True
        for k in range(2,n+1):
            for i in range(n-k+1):
                for j in range(n-k+1):
                    for t in range(1,k):
                        if dp[i][j][t] and dp[i+t][j+t][k-t]:
                            dp[i][j][k]=True
                            break
                        if dp[i][j+k-t][t] and dp[i+t][j][k-t]:
                            dp[i][j][k]=True
                            break
        return dp[0][0][n]




# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        length = len(s1)
        for i in range(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[length-i:]) and self.isScramble(s1[i:], s2[:length-i]):
                return True
        return False

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        s1 = "great", s2 = "rgeat"
    ), True),
    pytest.param(dict(  s1 = "abcde", s2 = "caebd" ), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isScramble(**kwargs) == expected
    assert Solution1().isScramble(**kwargs) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])