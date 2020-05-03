#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 22:33:41
# @Last Modified : 2020-05-03 22:33:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        """
        状态
        f[i][j] 表示 s 的第 i 个字符到第 j 个字符组成的子串中，最长的回文序列长度是多少。

        转移方程
        如果 s 的第 i 个字符和第 j 个字符相同的话

        f[i][j] = f[i + 1][j - 1] + 2

        如果 s 的第 i 个字符和第 j 个字符不同的话

        f[i][j] = max(f[i + 1][j], f[i][j - 1])

        然后注意遍历顺序，i 从最后一个字符开始往前遍历，j 从 i + 1 开始往后遍历，这样可以保证每个子问题都已经算好了。

        初始化
        f[i][i] = 1 单个字符的最长回文序列是 1

        结果
        f[0][n - 1]

        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


@pytest.mark.parametrize("args,expected", [
    ("bbbab", 4),
    pytest.param("cbbd", 2),
])
def test_solutions(args, expected):
    assert Solution().longestPalindromeSubseq(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
