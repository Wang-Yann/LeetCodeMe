#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。 
# 
#  注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。 
# 
#  
# 示例:
# 输入: 
# A = [9,1,2,3,9]
# K = 3
# 输出: 20
# 解释: 
# A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
# 我们也可以把 A 分成[9, 1], [2], [3, 9].
# 这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
#  
# 
#  说明: 
# 
#  
#  1 <= A.length <= 100. 
#  1 <= A[i] <= 10000. 
#  1 <= K <= A.length. 
#  答案误差在 10^-6 内被视为是正确的。 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        """
        我们可以使用动态规划来解决这个问题。设 dp( k,i) 表示将数组 A 中的前 i 个元素 A[:i] 分成 k 个相邻的非空子数组，
        可以得到的最大分数。
        """
        N = len(A)
        dp = [[0.0] * (N + 1) for _ in range(K + 1)]
        sums = [0.0] * (N + 1)
        for i in range(1, N + 1):
            sums[i] = sums[i - 1] + A[i - 1]
            dp[1][i] = 1.0 * sums[i] / i
        # print(dp,sums)
        for i in range(2, K + 1):
            for j in range(i, N + 1):
                for kk in range(i - 1, j):
                    dp[i][j] = 1.0 * max(dp[i][j], dp[i - 1][kk] + (sums[j] - sums[kk]) / (j - kk))
        return dp[K][N]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(A=[9, 1, 2, 3, 9], K=3), 20],
])
def test_solutions(kw, expected):
    assert Solution().largestSumOfAverages(**kw) == pytest.approx(expected, 1e-6)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
