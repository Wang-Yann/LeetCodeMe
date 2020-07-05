#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 16:48:39
# @Last Modified : 2020-07-05 16:48:39
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 m x n 的二进制矩阵 mat。 
# 
#  每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0 ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。（注：相邻的两个
# 单元格共享同一条边。） 
# 
#  请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。 
# 
#  二进制矩阵的每一个格子要么是 0 要么是 1 。 
# 
#  全零矩阵是所有格子都为 0 的矩阵。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：mat = [[0,0],[0,1]]
# 输出：3
# 解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。
#  
# 
#  示例 2： 
# 
#  输入：mat = [[0]]
# 输出：0
# 解释：给出的矩阵是全零矩阵，所以你不需要改变它。
#  
# 
#  示例 3： 
# 
#  输入：mat = [[1,1,1],[1,0,1],[0,0,0]]
# 输出：6
#  
# 
#  示例 4： 
# 
#  输入：mat = [[1,0,0],[1,0,0]]
# 输出：-1
# 解释：该矩阵无法转变成全零矩阵
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[0].length 
#  1 <= m <= 3 
#  1 <= n <= 3 
#  mat[i][j] 是 0 或 1 。 
#  
#  Related Topics 广度优先搜索 
#  👍 26 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minFlips(self, mat: List[List[int]]) -> int:
        """
        Q & A
        Q: Could you please further explain about the logic of transferring the matrix to int?
        sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
        I wonder how it works and why it works.

        A: For Input: mat = [[0,0],[0,1]], map it to 0b1000, that is, mapping mat[i][j] to the (i * n + j)th bit of an int. specifically,
        mat[0][0] = 0, corresponds to 0th bit, which is 0;
        mat[0][1] = 0, corresponds to 1st bit, which is 0;
        mat[1][0] = 0, corresponds to 2nd bit, which is 0;
        mat[1][1] = 1, corresponds to 3rd bit, which is 1;

        """
        m, n = len(mat), len(mat[0])
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
        # print(bin(start))
        dq = collections.deque([(start, 0)])
        seen = {start}
        while dq:
            cur, step = dq.popleft()
            if  cur==0:
                return step
            for i in range(m):
                for j in range(n):
                    nex = cur
                    for r, c in [(i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                        if 0 <= r <= m - 1 and 0 <= c <= n - 1:
                            nex ^= 1 << (r * n + c)
                    if nex not in seen:
                        seen.add(nex)
                        dq.append((nex, step + 1))
        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(mat=[[0, 0], [0, 1]]), 3),
    pytest.param(dict(mat=[[0]]), 0),
    pytest.param(dict(mat=[[1, 1, 1], [1, 0, 1], [0, 0, 0]]), 6),
    pytest.param(dict(mat=[[1, 0, 0], [1, 0, 0]]), -1),
])
def test_solutions(kwargs, expected):
    assert Solution().minFlips(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
