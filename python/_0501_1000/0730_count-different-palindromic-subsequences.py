#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 S，找出 S 中不同的非空回文子序列个数，并返回该数字与 10^9 + 7 的模。 
# 
#  通过从 S 中删除 0 个或多个字符来获得子序列。 
# 
#  如果一个字符序列与它反转后的字符序列一致，那么它是回文字符序列。 
# 
#  如果对于某个 i，A_i != B_i，那么 A_1, A_2, ... 和 B_1, B_2, ... 这两个字符序列是不同的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
# S = 'bccb'
# 输出：6
# 解释：
# 6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
# 注意：'bcb' 虽然出现两次但仅计数一次。
#  
# 
#  示例 2： 
# 
#  输入：
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# 输出：104860361
# 解释：
# 共有 3104860382 个不同的非空回文子序列，对 10^9 + 7 取模为 104860361。
#  
# 
#  
# 
#  提示： 
# 
#  
#  字符串 S 的长度将在[1, 1000]范围内。 
#  每个字符 S[i] 将会是集合 {'a', 'b', 'c', 'd'} 中的某一个。 
#  
# 
#  
#  Related Topics 字符串 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        """HARD   TODO
        https://leetcode-cn.com/problems/count-different-palindromic-subsequences/solution/tong-ji-bu-tong-hui-wen-zi-zi-fu-chuan-by-leetcode/
        定义 dp[x][i][j] 为子串 S[i...j] 拥有不同回文子字符串的答案，且 S[i] == S[j] == 'a'+x
        由于字符串只包含四个字符 a, b, c, d，因此 0 <= x < 4。dp 的公式如下：
            如果 S[i] != 'a'+x，则 dp[x][i][j] = dp[x][i+1][j]
            如果 S[j] != 'a'+x，则 dp[x][i][j] = dp[x][i][j-1]
            如果 S[i] == S[j] == 'a'+x，则 dp[x][i][j] = 2 + dp[0][i+1][j-1] + dp[1][i+1][j-1] + dp[2][i+1][j-1] + dp[3][i+1][j-1]。
                当第一个和最后一个字符相同时，我们需要计算子串 S[i+1][j-1] 中所有不同的回文（a、b、c、d 中的每一个）加上第一个和最后一个字符的两个回文。
            设 n 为字符串 S 的长度，则最终的答案为 dp[0][0][n-1] + dp[1][0][n-1] + dp[2][0][n-1] + dp[3][0][n-1] mod 1000000007
        """
        LEN = len(S)
        MOD = 1000000007
        dp = [[[0 for _ in range(LEN)] for _ in range(LEN)] for _ in range(4)]

        for i in range(LEN - 1, -1, -1):
            for j in range(i, LEN):
                for k in range(4):
                    char = chr(ord('a') + k)
                    if j == i:
                        if S[i] == char:
                            dp[k][i][j] = 1
                        else:
                            dp[k][i][j] = 0
                    else:  # j > i
                        if S[i] != char:
                            dp[k][i][j] = dp[k][i + 1][j]
                        elif S[j] != char:
                            dp[k][i][j] = dp[k][i][j - 1]
                        else:  # S[i] == S[j] == c
                            if j == i + 1:
                                dp[k][i][j] = 2  # "aa" : {"a", "aa"}
                            else:  # length is > 2
                                dp[k][i][j] = 2
                                for m in range(4):  # count each one within subwindows [i+1][j-1]
                                    dp[k][i][j] += dp[m][i + 1][j - 1]
                                    dp[k][i][j] %= MOD

        ans = 0
        for k in range(4):
            ans += dp[k][0][LEN - 1]
            ans %= MOD

        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ('bccb', 6),
    ('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba', 104860361),
])
def test_solutions(args, expected):
    assert Solution().countPalindromicSubsequences(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
