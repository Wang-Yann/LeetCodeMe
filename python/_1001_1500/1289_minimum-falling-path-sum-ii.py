#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数方阵 arr ，定义「非零偏移下降路径」为：从 arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。 
# 
#  请你返回非零偏移下降路径数字和的最小值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：13
# 解释：
# 所有非零偏移下降路径包括：
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# 下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length == arr[i].length <= 200 
#  -99 <= arr[i][j] <= 99 
#  
#  Related Topics 动态规划

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        M, N = len(arr), len(arr[0])
        for i in range(1, M):
            smallest_two = heapq.nsmallest(2, arr[i - 1])
            for j in range(N):
                if arr[i - 1][j] == smallest_two[0]:
                    arr[i][j] += smallest_two[1]
                else:
                    arr[i][j] += smallest_two[0]
        # print(arr)
        return min(arr[-1])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13)
])
def test_solutions(args, expected):
    assert Solution().minFallingPathSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
