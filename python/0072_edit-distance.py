#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 21:47:05
# @Last Modified : 2020-04-06 21:47:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
#  你可以对一个单词进行如下三种操作：
#
#
#  插入一个字符
#  删除一个字符
#  替换一个字符
#
#
#
#
#  示例 1：
#
#  输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
#  示例 2：
#
#  输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#  Related Topics 字符串 动态规划
#  👍 978 👎 0

"""
import pytest


class Solution:
    """我们用 D[i][j] 表示 A 的前 i 个字母和 B 的前 j 个字母之间的编辑距离。"""

    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)

        # 有一个字符串为空串
        if N1 * N2 == 0:
            return N1 + N2

        # DP 数组
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]

        # 边界状态初始化
        for i in range(N1 + 1):
            dp[i][0] = i
        for j in range(N2 + 1):
            dp[0][j] = j

        # 计算所有 DP 值

        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                delete = dp[i - 1][j] + 1
                insert = dp[i][j - 1] + 1
                replace = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                dp[i][j] = min(insert, delete, replace)

        return dp[N1][N2]


@pytest.mark.parametrize("kw,expected", [
    [dict(word1="horse", word2="ros"), 3],
    [dict(word1="intention", word2="execution"), 5],
])
def test_solutions(kw, expected):
    assert Solution().minDistance(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
