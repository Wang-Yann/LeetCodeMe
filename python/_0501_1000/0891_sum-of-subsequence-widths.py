#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 A ，考虑 A 的所有非空子序列。 
# 
#  对于任意序列 S ，设 S 的宽度是 S 的最大元素和最小元素的差。 
# 
#  返回 A 的所有子序列的宽度之和。 
# 
#  由于答案可能非常大，请返回答案模 10^9+7。 
# 
#  
# 
#  示例： 
# 
#  输入：[2,1,3]
# 输出：6
# 解释：
# 子序列为 [1]，[2]，[3]，[2,1]，[2,3]，[1,3]，[2,1,3] 。
# 相应的宽度是 0，0，0，1，1，2，2 。
# 这些宽度之和是 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20000 
#  1 <= A[i] <= 20000 
#  
#  Related Topics 数组 数学

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    HARD
    ∑ (2**i-2**(N-i-1))*Ai   (0<=i<=n-1)
​

       https://leetcode-cn.com/problems/sum-of-subsequence-widths/solution/zi-xu-lie-kuan-du-zhi-he-by-leetcode/
    """

    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N - 1 - i]) * x) % MOD
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([2, 1, 3], 6)
])
def test_solutions(args, expected):
    assert Solution().sumSubseqWidths(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
