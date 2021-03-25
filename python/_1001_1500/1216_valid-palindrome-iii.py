#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 17:24:01
# @Last Modified : 2020-08-05 17:24:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一个字符串 s 和一个整数 k，请你帮忙判断这个字符串是不是一个「K 回文」。 
# 
#  所谓「K 回文」：如果可以通过从字符串中删去最多 k 个字符将其转换为回文，那么这个字符串就是一个「K 回文」。 
# 
#  
# 
#  示例： 
# 
#  输入：s = "abcdeca", k = 2
# 输出：true
# 解释：删除字符 “b” 和 “e”。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 中只含有小写英文字母 
#  1 <= k <= s.length 
#  
#  Related Topics 字符串 动态规划 
#  👍 18 👎 0

"""
import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        N = len(s)

        @functools.lru_cache(None)
        def dp(l, r):
            if r <= l:
                return 0
            if s[l] == s[r]:
                return dp(l + 1, r - 1)
            else:
                return 1 + min(dp(l + 1, r), dp(l, r - 1))

        diff = dp(0, N - 1)
        return diff <= k


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        TODO
        没想到
        求字符串s和其反转字符串rs求最长公共子序列
        """
        N = len(s)

        def lcs(x, y):
            l = [[0] * (N + 1) for _ in range(N + 1)]
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if x[i - 1] == y[j - 1]:
                        l[i][j] = l[i - 1][j - 1] + 1
                    else:
                        l[i][j] = max(l[i - 1][j], l[i][j - 1])
            return l[-1][-1]

        return N - lcs(s, s[::-1]) <= k


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abcdeca", k=2), True],
])
def test_solutions(kw, expected):
    assert Solution().isValidPalindrome(**kw) == expected
    assert Solution1().isValidPalindrome(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
