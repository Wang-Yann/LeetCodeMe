#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们有两个长度相等且不为空的整型数组 A 和 B 。 
# 
#  我们可以交换 A[i] 和 B[i] 的元素。注意这两个元素在各自的序列中应该处于相同的位置。 
# 
#  在交换过一些元素之后，数组 A 和 B 都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.lengt
# h - 1]）。 
# 
#  给定数组 A 和 B ，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。 
# 
#  
# 示例:
# 输入: A = [1,3,5,4], B = [1,2,3,7]
# 输出: 1
# 解释: 
# 交换 A[3] 和 B[3] 后，两个数组如下:
# A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
# 两个数组均为严格递增的。 
# 
#  注意: 
# 
#  
#  A, B 两个数组的长度总是相等的，且长度的范围为 [1, 1000]。 
#  A[i], B[i] 均为 [0, 2000]区间内的整数。 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minSwap(self, A: List[int], B: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing/solution/leetcode-801-wo-gan-jio-ying-gai-jiang-de-hen-tou-/
        HARD
        dp[i][0]表示A和B [0, i] 的元素交换至有序, 并且不交换 A[i], B[i] 时的最小交换次数
        dp[i][1]表示A和B [0, i] 的元素交换至有序, 并且交换 A[i], B[i] 时的最小交换次数

        因为题目数据保证有解, 所以以下两个条件至少成立其中之一:
        1. A[i] > A[i - 1] && B[i] > B[i - 1]
        2. A[i] > B[i - 1] && B[i] > A[i - 1]

        当 1 成立时: dp[i][0] = min(dp[i - 1][0], dp[i][0]), dp[i][1] = min(dp[i - 1][1] + 1, dp[i][1])
        当 2 成立时: dp[i][0] = min(dp[i][0], dp[i - 1][1]), dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)
        注意两个条件有可能同时成立.
        边界: 除 dp0 = 0, dp0 = 1 之外, 其他状态初始值均为 INF.
        """
        lenA, lenB = map(len, (A, B))
        if lenA == 0 or lenA != lenB:
            return 0
        non_swapped, swapped = [0] * lenA, [1]+[0] * (lenA - 1)
        for i in range(1, lenA):
            swaps, non_swaps = set(), set()
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swaps.add(swapped[i - 1] + 1)
                non_swaps.add(non_swapped[i - 1])
            if B[i - 1] < A[i] and A[i - 1] < B[i]:
                swaps.add(non_swapped[i - 1] + 1)
                non_swaps.add(swapped[i - 1])
            # print(swaps,non_swaps)
            swapped[i], non_swapped[i] = min(swaps), min(non_swaps)
        return min(swapped[-1], non_swapped[-1])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=[1, 3, 5, 4], B=[1, 2, 3, 7]), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().minSwap(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
