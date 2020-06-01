#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。 
# 
#  例如，以下数列为等差数列: 
# 
#  1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9 
# 
#  以下数列不是等差数列。 
# 
#  1, 1, 2, 5, 7 
# 
#  
# 
#  数组 A 包含 N 个数，且索引从 0 开始。该数组子序列将划分为整数序列 (P0, P1, ..., Pk)，P 与 Q 是整数且满足 0 ≤ P0 <
#  P1 < ... < Pk < N。 
# 
#  
# 
#  如果序列 A[P0]，A[P1]，...，A[Pk-1]，A[Pk] 是等差的，那么数组 A 的子序列 (P0，P1，…，PK) 称为等差序列。值得注意的
# 是，这意味着 k ≥ 2。 
# 
#  函数要返回数组 A 中所有等差子序列的个数。 
# 
#  输入包含 N 个整数。每个整数都在 -231 和 231-1 之间，另外 0 ≤ N ≤ 1000。保证输出小于 231-1。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：[2, 4, 6, 8, 10]
# 
# 输出：7
# 
# 解释：
# 所有的等差子序列为：
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#  
# 
#  
#  Related Topics 动态规划

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    dp[i][k]都是表示到数组第i为底公差为k的数列的个数
    dp[i][k] += 1 + dp[j][k], j < i
https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/solution/deng-chai-shu-lie-hua-fen-ii-zi-xu-lie-by-leetcode/

    """

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length = len(A)
        dp = [collections.defaultdict(int) for _ in range(length)]
        res = 0
        for i in range(length):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff] + 1
                # 说明满足长度大于等于3
                if diff in dp[j]:
                    res += dp[j][diff]
        # print(dp)
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([2, 4, 6, 8, 10], 7),
])
def test_solutions(args, expected):
    assert Solution().numberOfArithmeticSlices(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
