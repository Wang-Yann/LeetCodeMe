#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定由若干 0 和 1 组成的矩阵 matrix，从中选出任意数量的列并翻转其上的 每个 单元格。翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 
# 。 
# 
#  返回经过一些翻转后，行上所有值都相等的最大行数。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：[[0,1],[1,1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。
#  
# 
#  示例 2： 
# 
#  输入：[[0,1],[1,0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。
#  
# 
#  示例 3： 
# 
#  输入：[[0,0,0],[0,0,1],[1,1,0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= matrix.length <= 300 
#  1 <= matrix[i].length <= 300 
#  所有 matrix[i].length 都相等 
#  matrix[i][j] 为 0 或 1 
#  
#  Related Topics 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        如果两个行是可以通过翻转相同的列达到全行相同，那么就要满足，两行的相同的位置上的值异或之后等于全1
        """
        counter = collections.Counter(tuple(x ^ row[0] for x in row) for row in matrix)
        # print(counter)
        return max(counter.values())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[0, 1], [1, 1]], 1),
    ([[0, 1], [1, 0]], 2),
    ([[0, 0, 0], [0, 0, 1], [1, 1, 0]], 2),
])
def test_solutions(args, expected):
    assert Solution().maxEqualRowsAfterFlips(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
