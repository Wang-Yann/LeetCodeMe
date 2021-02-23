#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 10:44:26
# @Last Modified : 2021-02-23 10:44:26
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个字符串 word1 和 word2 ，请你按下述方法构造一个字符串： 
# 
#  
#  从 word1 中选出某个 非空 子序列 subsequence1 。 
#  从 word2 中选出某个 非空 子序列 subsequence2 。 
#  连接两个子序列 subsequence1 + subsequence2 ，得到字符串。 
#  
# 
#  返回可按上述方法构造的最长 回文串 的 长度 。如果无法构造回文串，返回 0 。 
# 
#  字符串 s 的一个 子序列 是通过从 s 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。 
# 
#  回文串 是正着读和反着读结果一致的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：word1 = "cacb", word2 = "cbba"
# 输出：5
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。 
# 
#  示例 2： 
# 
#  输入：word1 = "ab", word2 = "ab"
# 输出：3
# 解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。 
# 
#  示例 3： 
# 
#  输入：word1 = "aa", word2 = "bb"
# 输出：0
# 解释：无法按题面所述方法构造回文串，所以返回 0 。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word1.length, word2.length <= 1000 
#  word1 和 word2 由小写英文字母组成 
#  
#  Related Topics 动态规划 
#  👍 17 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        N = len(s)
        dp = [[0] * N for _ in range(N)]  # 关注区间的两个端点
        for i in range(N):
            dp[i][i] = 1
        res = 0
        for i in range(N - 1, -1, -1):  # 顺序是由dp关系式决定的
            for j in range(i + 1, N):  #
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < len(word1) <= j:  # 保证i是word1的，j是word2的
                        res = max(res, dp[i][j])  # 有增加才更新res
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # 没有增加，不用更新

        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(word1="cacb", word2="cbba"), 5],
    [dict(word1="ab", word2="ab"), 3],
    [dict(word1="aa", word2="bb"), 0],
])
def test_solutions(kw, expected):
    assert Solution().longestPalindrome(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
