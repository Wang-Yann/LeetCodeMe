#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-26 22:22:34
# @Last Modified : 2020-07-26 22:22:34
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定字符串 S and T，找出 S 中最短的（连续）子串 W ，使得 T 是 W 的 子序列 。 
# 
#  如果 S 中没有窗口可以包含 T 中的所有字符，返回空字符串 ""。如果有不止一个最短长度的窗口，返回开始位置最靠左的那个。 
# 
#  示例 1： 
# 
#  输入：
# S = "abcdebdde", T = "bde"
# 输出："bcde"
# 解释：
# "bcde" 是答案，因为它在相同长度的字符串 "bdde" 出现之前。
# "deb" 不是一个更短的答案，因为在窗口中必须按顺序出现 T 中的元素。 
# 
#  
# 
#  注： 
# 
#  
#  所有输入的字符串都只包含小写字母。All the strings in the input will only contain lowercase let
# ters. 
#  S 长度的范围为 [1, 20000]。 
#  T 长度的范围为 [1, 100]。 
#  
# 
#  
#  Related Topics 动态规划 Sliding Window 
#  👍 38 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minWindow(self, S: str, T: str) -> str:
        """
        GOOD
        首先通过预处理的方式计算 next[i][letter]，使其表示 S[i:] 中第一个出现的 letter 的位置，如果不存在则用 -1 表示。
        随后递增 j，找到包含 T[:j] 的窗口。最终遍历所有窗口，找到其中的最小窗口。
        链接：https://leetcode-cn.com/problems/minimum-window-subsequence/solution/zui-xiao-chuang-kou-zi-xu-lie-by-leetcode/

        """
        N = len(S)
        nex = [None] * N
        last = [-1] * 26
        for i in range(N - 1, -1, -1):
            last[ord(S[i]) - ord('a')] = i
            nex[i] = tuple(last)
        # print(nex)

        windows = [[i, i] for i, c in enumerate(S) if c == T[0]]
        for j in range(1, len(T)):
            letter_index = ord(T[j]) - ord('a')
            windows = [[root, nex[i + 1][letter_index]]
                       for root, i in windows
                       if 0 <= i < N - 1 and nex[i + 1][letter_index] >= 0]
        # print(windows)
        if not windows:
            return ""
        i, j = min(windows, key=lambda x:x[1] - x[0])
        return S[i: j + 1]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def minWindow(self, S: str, T: str) -> str:
        """
        dpi表示匹配T串的前i个字符，S中前j个字符中匹配的起点，当前两字符相同时，则有dpi = dpi-1，当两字符不相同时，相当于第j个字符被跳过，则有dpi = dpi
        """

        # Write your code here
        NT, NS = len(T), len(S)
        dp = [[0] * (NS + 1) for _ in range(NT + 1)]
        for i in range(0, NS + 1):
            dp[0][i] = i + 1  # 初始化两字符串匹配的起点
        for i in range(1, NT + 1):  # T字符串
            for j in range(1, NS + 1):  # S字符串
                if T[i - 1] == S[j - 1]:  # 两字符匹配
                    dp[i][j] = dp[i - 1][j - 1]  # dp[i][j]的起点则等于dp[i-1][j-1]的起点
                else:
                    dp[i][j] = dp[i][j - 1]  # dp[i][j]的起点等于dp[i][j-1]的起点
        start, length = 0, NS + 1
        for i in range(1, NS + 1):
            if dp[NT][i] != 0:  # dp[m][j]!=0表示当前T串的m个字符已经匹配成为S串的前j个长度字符串的子序列
                if i - dp[NT][i] + 1 < length:  # 选择字符串长度最小的
                    start = dp[NT][i] - 1
                    length = i - dp[NT][i] + 1
        if length == NS + 1:
            return ""
        return S[start:start + length]


@pytest.mark.parametrize("kwargs,expected", [
    [dict(S="abcdebdde", T="bde"), "bcde"],
    [dict(
        S="fgrqsqsnodwmxzkzxwqegkndaa",
        T="fnok"
    ),
        "fgrqsqsnodwmxzk"],
])
def test_solutions(kwargs, expected):
    assert Solution().minWindow(**kwargs) == expected
    assert Solution1().minWindow(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
