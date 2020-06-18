#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。 
# 
#  （如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列） 
# 
#  
# 
#  示例： 
# 
#  输入：str1 = "abac", str2 = "cab"
# 输出："cabac"
# 解释：
# str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
# str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
# 最终我们给出的答案是满足上述属性的最短字符串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= str1.length, str2.length <= 1000 
#  str1 和 str2 都由小写英文字母组成。 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[""] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
        i = j = 0
        lcs = dp[m][n]
        ans = ""
        for char in lcs:
            while i < m and str1[i] != char:
                ans += str1[i]
                i += 1
            while j < n and str2[j] != char:
                ans += str2[j]
                j += 1
            ans += char
            i += 1
            j += 1
        return ans + str1[i:] + str2[j:]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(str1="abac", str2="cab"), "cabac"],
])
def test_solutions(kw, expected):
    assert Solution().shortestCommonSupersequence(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
