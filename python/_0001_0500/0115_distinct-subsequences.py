#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。 
# 
#  一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是） 
# 
#  题目数据保证答案符合 32 位带符号整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "rabbbit", T = "rabbit"
# 输出：3
# 解释：
# 
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#  
# 
#  示例 2： 
# 
#  输入：S = "babgbag", T = "bag"
# 输出：5
# 解释：
# 
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^ 
#  Related Topics 字符串 动态规划

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        NS, NT = len(s), len(t)
        dp = [[0] * (NT + 1) for _ in range(NS + 1)]
        for i in range(NS + 1):
            dp[i][0] = 1
        for i in range(NS):
            for j in range(NT):
                if s[i] == t[j]:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
        return dp[NS][NT]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="rabbbit", t="rabbit"), 3),
    pytest.param(dict(s="babgbag", t="bag"), 5),
])
def test_solutions(kwargs, expected):
    assert Solution().numDistinct(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
