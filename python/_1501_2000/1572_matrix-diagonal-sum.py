#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 03:48:47
# @Last Modified : 2021-02-24 03:48:47
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。 
# 
#  请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：mat = [[1,2,3],
#             [4,5,6],
#             [7,8,9]]
# 输出：25
# 解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
# 请注意，元素 mat[1][1] = 5 只会被计算一次。
#  
# 
#  示例 2： 
# 
#  
# 输入：mat = [[1,1,1,1],
#             [1,1,1,1],
#             [1,1,1,1],
#             [1,1,1,1]]
# 输出：8
#  
# 
#  示例 3： 
# 
#  
# 输入：mat = [[5]]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == mat.length == mat[i].length 
#  1 <= n <= 100 
#  1 <= mat[i][j] <= 100 
#  
#  Related Topics 数组 
#  👍 22 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        ans = sum(mat[i][i] + mat[N - 1 - i][i] for i in range(N))
        if N % 2 == 1:
            ans -= mat[N // 2][N // 2]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25],
    [dict(mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]), 8],
    [dict(mat=[[5]]), 5],
    [dict(mat=[[7, 3, 1, 9],
               [3, 4, 6, 9],
               [6, 9, 6, 6],
               [9, 5, 8, 5]]), 55],
])
def test_solutions(kw, expected):
    assert Solution().diagonalSum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
