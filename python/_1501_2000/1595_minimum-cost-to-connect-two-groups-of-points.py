#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 06:17:28
# @Last Modified : 2021-02-22 06:17:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两组点，其中第一组中有 size1 个点，第二组中有 size2 个点，且 size1 >= size2 。 
# 
#  任意两点间的连接成本 cost 由大小为 size1 x size2 矩阵给出，其中 cost[i][j] 是第一组中的点 i 和第二组中的点 j 的连接
# 成本。如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至
# 少与第一组中的一个点连接。 
# 
#  返回连通两组点所需的最小成本。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：cost = [[15, 96], [36, 2]]
# 输出：17
# 解释：连通两组点的最佳方法是：
# 1--A
# 2--B
# 总成本为 17 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# 输出：4
# 解释：连通两组点的最佳方法是：
# 1--A
# 2--B
# 2--C
# 3--A
# 最小成本为 4 。
# 请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需要关心最低总成本。 
# 
#  示例 3： 
# 
#  输入：cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
# 输出：10
#  
# 
#  
# 
#  提示： 
# 
#  
#  size1 == cost.length 
#  size2 == cost[i].length 
#  1 <= size1, size2 <= 12 
#  size1 >= size2 
#  0 <= cost[i][j] <= 100 
#  
#  Related Topics 图 动态规划 
#  👍 33 👎 0

"""

import functools
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        """状态压缩"""
        M, N = len(cost), len(cost[0])
        min_arr = [min(x) for x in zip(*cost)]
        # print(min_arr)

        @functools.lru_cache(None)
        def dp(i, mask):
            if i == M:
                ans = 0
                for j in range(N):
                    if not (mask & (1 << j)):
                        ans += min_arr[j]
                return ans
            ans = math.inf
            for j in range(N):
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return ans

        return dp(0, 0)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(cost=[[15, 96], [36, 2]]), 17],
    [dict(cost=[[1, 3, 5], [4, 1, 1], [1, 5, 3]]), 4],
    [dict(cost=[[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]), 10],
])
def test_solutions(kw, expected):
    assert Solution().connectTwoGroups(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
