#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。 
# 
#  请你返回让 s 成为回文串的 最少操作次数 。 
# 
#  「回文串」是正读和反读都相同的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "zzazz"
# 输出：0
# 解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "mbadm"
# 输出：2
# 解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "leetcode"
# 输出：5
# 解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "g"
# 输出：0
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "no"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 中所有字符都是小写字母。 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minInsertions(self, s: str) -> int:
        """
        区间DP
        我们用 dp[i][j] 表示对于字符串 s 的子串 s[i:j]（这里的下标从 0 开始，并且 s[i:j] 包含 s 中的第 i 和第 j 个字符），
        最少添加的字符数量，使得 s[i:j] 变为回文串
        dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j - 1] + 1)                     if s[i] != s[j]
        dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j - 1] + 1, dp[i + 1][j - 1])   if s[i] == s[j]
        """
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for l in range(2, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])
        return dp[0][N - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("zzazz", 0),
    ("mbadm", 2),
    ("leetcode", 5),
    ("g", 0),
    ("no", 1),
])
def test_solutions(args, expected):
    assert Solution().minInsertions(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
