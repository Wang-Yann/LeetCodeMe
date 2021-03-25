#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。 
# 
#  一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。 
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
#  
# 
#  若这两个字符串没有公共子序列，则返回 0。 
# 
#  
# 
#  示例 1: 
# 
#  输入：text1 = "abcde", text2 = "ace" 
# 输出：3  
# 解释：最长公共子序列是 "ace"，它的长度为 3。
#  
# 
#  示例 2: 
# 
#  输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
#  
# 
#  示例 3: 
# 
#  输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= text1.length <= 1000 
#  1 <= text2.length <= 1000 
#  输入的字符串只含有小写英文字符。 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = map(len, (text1, text2))
        if not (N1 and N2):
            return 0
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[N1][N2]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(text1="abcde", text2="ace"), 3],
    [dict(text1="abc", text2="abc"), 3],
    [dict(text1="abc", text2="def"), 0],
])
def test_solutions(kw, expected):
    assert Solution().longestCommonSubsequence(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
