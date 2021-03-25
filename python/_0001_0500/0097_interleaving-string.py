#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。 
# 
#  示例 1: 
# 
#  输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false 
#  Related Topics 字符串 动态规划

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        dp[i][j]代表由s1的前i个字母和s2的前j个字母是否能构成当前i+j个字母。
然后状态转移即可。（看第i+j+1个是否能被s1的第i+1个构成或被s2的第j+1个构成）
        """

        len_s1, len_s2, len_s3 = map(len, (s1, s2, s3))
        if len_s1 + len_s2 != len_s3:
            return False
        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        dp[0][0] = True
        for i in range(len_s1):
            dp[i + 1][0] = s1[:i + 1] == s3[:i + 1]
        for j in range(len_s2):
            dp[0][j + 1] = s2[:j + 1] == s3[:j + 1]
        for i in range(len_s1):
            for j in range(len_s2):
                if s1[i] == s3[i + j + 1]:
                    dp[i + 1][j + 1] |= dp[i][j + 1]
                if s2[j] == s3[i + j + 1]:
                    dp[i + 1][j + 1] |= dp[i + 1][j]
        return dp[len_s1][len_s2]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        s1="aabcc", s2="dbbca", s3="aadbbcbcac"
    ), True),
    pytest.param(dict(s1="aabcc", s2="dbbca", s3="aadbbbaccc"), False),
    pytest.param(dict(s1="ab", s2="bc", s3="babc"), True),
])
def test_solutions(kwargs, expected):
    assert Solution().isInterleave(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
