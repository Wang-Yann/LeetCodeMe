#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出矩阵 matrix 和目标值 target，返回元素总和等于目标值的非空子矩阵的数量。 
# 
#  子矩阵 x1, y1, x2, y2 是满足 x1 <= x <= x2 且 y1 <= y <= y2 的所有单元 matrix[x][y] 的集合。 
# 
# 
#  如果 (x1, y1, x2, y2) 和 (x1', y1', x2', y2') 两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵
# 也不同。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# 输出：4
# 解释：四个只含 0 的 1x1 子矩阵。
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,-1],[-1,1]], target = 0
# 输出：5
# 解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= matrix.length <= 300 
#  1 <= matrix[0].length <= 300 
#  -1000 <= matrix[i] <= 1000 
#  -10^8 <= target <= 10^8 
#  
#  Related Topics 数组 动态规划 Sliding Window

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target/solution/25xing-dai-ma-zhuan-hua-wei-yi-wei-subarray-sum-by/
        通过(i,j)，定位矩形的始末行。sum 记录矩形内每个长条的和，这样问题转化为求一维的 subarray sum。
因为有负值，无法使用单调性优化。可以使用map 保存已有的sum，cur-target = sum ，就代表找到一个可行解

        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
        count = 0
        for i in range(m):
            prefix_sum = [0] * n
            for j in range(i, m):
                counter = collections.Counter({0:1})
                for k in range(n):
                    prefix_sum[k] += matrix[j][k]
                    count += counter[prefix_sum[k] - target]
                    counter[prefix_sum[k]] += 1
        return count


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0
    ), 4),
    pytest.param(dict(matrix=[[1, -1], [-1, 1]], target=0), 5),
])
def test_solutions(kwargs, expected):
    assert Solution().numSubmatrixSumTarget(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
