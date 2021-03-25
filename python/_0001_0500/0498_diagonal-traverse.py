#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。 
# 
#  
# 
#  示例: 
# 
#  输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 
# 输出:  [1,2,4,7,5,3,6,8,9]
# 
# 解释:
# 
#  
# 
#  
# 
#  说明: 
# 
#  
#  给定矩阵中的元素总数不会超过 100000 。 
#  
# 

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        (0,0),(0,1),(1,0),(2,0),(1,1),(0,2),(1,2),(2,1),(2,2)
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        dd = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                dd[i + j + 1].append(matrix[i][j])
        # print(dd)
        res = []
        for k, v in dd.items():
            if k % 2 == 1:
                dd[k].reverse()
            res.extend(dd[k])
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
])
def test_solutions(args, expected):
    assert Solution().findDiagonalOrder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
