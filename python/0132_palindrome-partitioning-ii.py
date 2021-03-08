#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。 
# 
#  返回符合要求的最少分割次数。 
# 
#  示例: 
# 
#  输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
#  Related Topics 动态规划

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minCut(self, s: str) -> int:
        """
        dp[i]：表示前缀子串 s[0:i] 分割成若干个回文子串所需要最小分割次数
        """

        def is_palindrome(l, r):
            return s[l:r + 1] == s[l:r + 1][::-1]

        N = len(s)
        if N < 2:
            return 0
        dp = [0] * N
        for i in range(1, N):
            if is_palindrome(0, i):
                dp[i] = 0
                continue
            dp[i] = min([dp[j] + 1 for j in range(i) if is_palindrome(j + 1, i)])
        return dp[N - 1]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def minCut(self, s: str) -> int:
        """
        dp_g(i,j) 表示 s[i..j] 是否为回文串
        """
        N = len(s)
        dp_g = [[True] * N for _ in range(N)]

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                dp_g[i][j] = (s[i] == s[j]) and dp_g[i + 1][j - 1]

        dp = [0x7fffffff] * N
        for i in range(N):
            if dp_g[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if dp_g[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[N - 1]


@pytest.mark.parametrize("kw,expected", [
    [dict(s="aab"), 1],
    [dict(s="a"), 0],
    [dict(s="ab"), 1],
    [dict(s="leet"), 2],
])
@pytest.mark.parametrize("SolutionCls", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCls):
    assert SolutionCls().minCut(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
