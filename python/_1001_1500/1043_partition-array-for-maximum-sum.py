#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出整数数组 A，将该数组分隔为长度最多为 K 的几个（连续）子数组。分隔完成后，每个子数组的中的值都会变为该子数组中的最大值。 
# 
#  返回给定数组完成分隔后的最大和。 
# 
#  
# 
#  示例： 
# 
#  输入：A = [1,15,7,9,2,5,10], K = 3
# 输出：84
# 解释：A 变为 [15,15,15,9,10,10,10] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= K <= A.length <= 500 
#  0 <= A[i] <= 10^6 
#  

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        """
        dp[i] record the maximum sum we can get considering A[0] ~ A[i]
        To get dp[i], we will try to change k last numbers separately to the maximum of them,
        where k = 1 to k = K.

        """
        N = len(A)
        dp = [0] * N
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
                # print(i,k,curMax)

        # print(dp)
        return dp[N - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=[1, 15, 7, 9, 2, 5, 10], K=3), 84),
])
def test_solutions(kwargs, expected):
    assert Solution().maxSumAfterPartitioning(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
