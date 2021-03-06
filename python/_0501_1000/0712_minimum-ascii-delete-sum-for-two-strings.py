#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。 
# 
#  示例 1: 
# 
#  
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
#  
# 
#  示例 2: 
# 
#  
# 输入: s1 = "delete", s2 = "leet"
# 输出: 403
# 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
# 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
# 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
# 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
#  
# 
#  注意: 
# 
#  
#  0 < s1.length, s2.length <= 1000。 
#  所有字符串中的字符ASCII值在[97, 122]之间。 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        我们用 dp[i][j] 表示字符串 s1[:i] 和 s2[:j]
        达到相等所需删除的字符的 ASCII 值的最小和

        """
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(len1):
            dp[i + 1][0] = dp[i][0] + ord(s1[i])
        for j in range(len2):
            dp[0][j + 1] = dp[0][j] + ord(s2[j])
        for i in range(len1):
            for j in range(len2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(
                        dp[i][j + 1] + ord(s1[i]),
                        dp[i + 1][j] + ord(s2[j])
                    )
        # print(dp)
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s1="sea", s2="eat"), 231],
    [dict(s1="delete", s2="leet"), 403],
    [dict(s1="ccaccjp", s2="fwosarcwge"), 1399],
])
def test_solutions(kw, expected):
    assert Solution().minimumDeleteSum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
