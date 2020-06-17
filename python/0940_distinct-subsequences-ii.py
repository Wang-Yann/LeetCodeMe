#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 S，计算 S 的不同非空子序列的个数。 
# 
#  因为结果可能很大，所以返回答案模 10^9 + 7. 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：7
# 解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
#  
# 
#  示例 2： 
# 
#  输入："aba"
# 输出：6
# 解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
#  
# 
#  示例 3： 
# 
#  输入："aaa"
# 输出：3
# 解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  S 只包含小写字母。 
#  1 <= S.length <= 2000 
#  
# 
#  
# 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        """以每个字符为结尾的字符串数量，再对总的求和
        上次的结果加上当前字符　，考虑字典树的样式
        https://blog.csdn.net/qq_17550379/article/details/84105392
        """
        MOD = 10 ** 9 + 7
        dp = [0] * 26
        for char in S:
            dp[ord(char) - ord("a")] = sum(dp) + 1
            # print(dp)
        return sum(dp) % MOD


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    """
    https://leetcode-cn.com/problems/distinct-subsequences-ii/solution/bu-tong-de-zi-xu-lie-ii-by-leetcode/
    不好想DP
    """
    def distinctSubseqII(self, S):
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i

        return (dp[-1] - 1) % (10 ** 9 + 7)


class Solution2(object):
    def distinctSubseqII(self, S):
        M = 10 ** 9 + 7
        result, dp = 0, [0] * 26
        for c in S:
            result, dp[ord(c) - ord('a')] = 2 * result - dp[ord(c) - ord('a')] + 1, result + 1
        return result % M


@pytest.mark.parametrize("args,expected", [
    ("abc", 7),
    ("abcaaad", 57),
    ("aba", 6),
    ("aaa", 3),
])
def test_solutions(args, expected):
    assert Solution().distinctSubseqII(args) == expected
    assert Solution1().distinctSubseqII(args) == expected
    assert Solution2().distinctSubseqII(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
