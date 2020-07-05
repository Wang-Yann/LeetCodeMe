#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 22:51:20
# @Last Modified : 2020-07-05 22:51:20
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。 
# 
#  给你一个字符串 s，请你返回它的 最长快乐前缀。 
# 
#  如果不存在满足题意的前缀，则返回一个空字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "level"
# 输出："l"
# 解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel
# "）。最长的既是前缀也是后缀的字符串是 "l" 。
#  
# 
#  示例 2： 
# 
#  输入：s = "ababab"
# 输出："abab"
# 解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
#  
# 
#  示例 3： 
# 
#  输入：s = "leetcodeleet"
# 输出："leet"
#  
# 
#  示例 4： 
# 
#  输入：s = "a"
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s 只含有小写英文字母 
#  
#  Related Topics 字符串 
#  👍 40 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestPrefix(self, s: str) -> str:
        """
        GOOD GOOD TODO
        Rabin-Karp
        对于前缀而言，每在字符串最后多出一个新的字符，就相当于原编码值乘以 \textit{base}base 再加上新的字符的编码值；
        对于后缀而言，每在字符串最前多出一个新的字符，就相当于原编码值加上新的字符的编码值乘以 \textit{base}base 的 i-1i−1 次幂。

        """
        N = len(s)
        prefix = suffix = 0
        BASE, MOD, MUL = 31, 10 ** 9 + 7, 1
        happy = 0
        for i in range(1, N):
            prefix = (prefix * BASE + (ord(s[i - 1]) - ord("a"))) % MOD
            suffix = (suffix + (ord(s[N - i]) - ord("a")) * MUL) % MOD
            if prefix == suffix:
                happy = i
            MUL = MUL * BASE % MOD
        return s[:happy]


# leetcode submit region end(Prohibit modification and deletion)


class SolutionKMP:

    def longestPrefix(self, s: str) -> str:
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in range(1, len(pattern)):
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = prefix[j]
                if pattern[j + 1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix
        pre_arr = getPrefix(s)
        # print(pre_arr)
        happy =pre_arr[-1]
        return s[:happy + 1]


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="level"), "l"),
    pytest.param(dict(s="ababab"), "abab"),
    pytest.param(dict(s="leetcodeleet"), "leet"),
    pytest.param(dict(s="a"), ""),
])
def test_solutions(kwargs, expected):
    assert Solution().longestPrefix(**kwargs) == expected
    assert SolutionKMP().longestPrefix(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
