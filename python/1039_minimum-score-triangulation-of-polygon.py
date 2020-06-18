#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定 N，想象一个凸 N 边多边形，其顶点按顺时针顺序依次标记为 A[0], A[i], ..., A[N-1]。 
# 
#  假设您将多边形剖分为 N-2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 N-2 个三角形的值之和。 
# 
#  返回多边形进行三角剖分后可以得到的最低分。 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3]
# 输出：6
# 解释：多边形已经三角化，唯一三角形的分数为 6。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[3,7,4,5]
# 输出：144
# 解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。
#  
# 
#  示例 3： 
# 
#  输入：[1,3,1,4,1,5]
# 输出：13
# 解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= A.length <= 50 
#  1 <= A[i] <= 100 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for l in range(3, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                # print(l,i,j)
                dp[i][j] = float("inf")
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])
        # print(dp)
        return dp[0][N - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3], 6),
    ([3, 7, 4, 5], 144),
    ([1, 3, 1, 4, 1, 5], 13),
])
def test_solutions(args, expected):
    assert Solution().minScoreTriangulation(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])