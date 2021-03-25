#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们给出 S，一个源于 {'D', 'I'} 的长度为 n 的字符串 。（这些字母代表 “减少” 和 “增加”。） 
# 有效排列 是对整数 {0, 1, ..., n} 的一个排列 P[0], P[1], ..., P[n]，使得对所有的 i： 
# 
#  
#  如果 S[i] == 'D'，那么 P[i] > P[i+1]，以及； 
#  如果 S[i] == 'I'，那么 P[i] < P[i+1]。 
#  
# 
#  有多少个有效排列？因为答案可能很大，所以请返回你的答案模 10^9 + 7. 
# 
#  
# 
#  示例： 
# 
#  输入："DID"
# 输出：5
# 解释：
# (0, 1, 2, 3) 的五个有效排列是：
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 200 
#  S 仅由集合 {'D', 'I'} 中的字符组成。 
#  
# 
#  
#  Related Topics 分治算法 动态规划

"""
import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:

    def numPermsDISequence(self, S):
        """
        https://leetcode-cn.com/problems/valid-permutations-for-di-sequence/solution/di-xu-lie-de-you-xiao-pai-lie-by-leetcode/
        TODO TODO
        HARD
        我们用 dp(i, j) 表示确定了排列中到 P[i] 为止的前 i + 1 个元素，并且 P[i] 和未选择元素的相对大小为 j 的方案数（即未选择的元素中，有 j 个元素比 P[i] 小）。在状态转移时，dp(i, j) 会从 dp(i - 1, k) 转移而来，其中 k 代表了 P[i - 1] 的相对大小。如果 S[i - 1] 为 D，那么 k 不比 j 小；如果 S[i - 1] 为 I，那么 k 必须比 j 小。

        """
        MOD = 10 ** 9 + 7
        N = len(S)

        @functools.lru_cache(None)
        def dp(i, j):
            # How many ways to place P_i with relative rank j?
            if not (0 <= j <= i):
                return 0
            if i == 0:
                return 1
            elif S[i - 1] == 'D':
                return (dp(i, j + 1) + dp(i - 1, j)) % MOD
            else:
                return (dp(i, j - 1) + dp(i - 1, j - 1)) % MOD

        return sum(dp(N, j) for j in range(N + 1)) % MOD


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def numPermsDISequence(self, S: str) -> int:
        """
        Difficult
        dp[i][j]代表符合DI规则的前i个位置的由j结尾的数组的数目，递推公式：
        DI字符串在i位置是'D'：dp[i][j] += dp[i-1][k] for k >= j
        DI字符串在i位置是'I'：dp[i][j] += dp[i-1][k] for k < j
        由递推公式可以看出需要dp[i][0],dp[i][1],...,dp[i][j]的和，改变dp[i][j]的意义，dp[i][j]此时代表前述的和，添加dp[i][j]+=dp[i][j-1]

        """
        dp = [1] * (len(S) + 1)
        for char in S:
            if char == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10 ** 9 + 7)


@pytest.mark.parametrize("args,expected", [
    ("DID", 5),
])
def test_solutions(args, expected):
    assert Solution().numPermsDISequence(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
