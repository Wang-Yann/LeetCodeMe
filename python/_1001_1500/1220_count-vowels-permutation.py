#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串： 
# 
#  
#  字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'） 
#  每个元音 'a' 后面都只能跟着 'e' 
#  每个元音 'e' 后面只能跟着 'a' 或者是 'i' 
#  每个元音 'i' 后面 不能 再跟着另一个 'i' 
#  每个元音 'o' 后面只能跟着 'i' 或者是 'u' 
#  每个元音 'u' 后面只能跟着 'a' 
#  
# 
#  由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
#  
# 
#  示例 3： 
# 
#  输入：n = 5
# 输出：68 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2 * 10^4 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countVowelPermutation(self, n: int) -> int:
        """
          AC 纪念
           lookup = {
                  "a": ["e"],
                  "e": ["a", "i"],
                  "i": ["a", "e", "o", "u"],
                  "o": ["i", "u"],
                  "u": ["a"],
              }
          """
        MOD = 10 ** 9 + 7
        dp = {}
        CHOICES = "aeiou"
        for k in CHOICES:
            dp[k] = [1] + [0] * (n - 1)
        for i in range(1, n):
            dp["a"][i] = (dp["e"][i - 1] + dp["i"][i - 1] + dp["u"][i - 1]) % MOD
            dp["e"][i] = (dp["a"][i - 1] + dp["i"][i - 1]) % MOD
            dp["i"][i] = (dp["e"][i - 1] + dp["o"][i - 1]) % MOD
            dp["o"][i] = (dp["i"][i - 1]) % MOD
            dp["u"][i] = (dp["i"][i - 1] + dp["o"][i - 1]) % MOD
        # print(dp)
        return sum(dp[k][-1] for k in CHOICES) % MOD


# leetcode submit region end(Prohibit modification and deletion)


# Time:  O(n)
# Space: O(1)
class Solution1(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i, (i + o) % MOD
        return (a + e + i + o + u) % MOD


@pytest.mark.parametrize("args,expected", [
    (1, 5),
    (2, 10),
    (5, 68),
])
def test_solutions(args, expected):
    assert Solution().countVowelPermutation(args) == expected
    assert Solution1().countVowelPermutation(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
