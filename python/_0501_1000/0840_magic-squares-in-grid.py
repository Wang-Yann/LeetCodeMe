#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。 
# 
#  给定一个由整数组成的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。 
# 
#  
# 
#  示例： 
# 
#  输入: [[4,3,8,4],
#       [9,5,1,9],
#       [2,7,6,2]]
# 输出: 1
# 解释: 
# 下面的子矩阵是一个 3 x 3 的幻方：
# 438
# 951
# 276
# 
# 而这一个不是：
# 384
# 519
# 762
# 
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
#  
# 
#  提示: 
# 
#  
#  1 <= grid.length <= 10 
#  1 <= grid[0].length <= 10 
#  0 <= grid[i][j] <= 15 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(r, c):
            m = [row[c:c + 3] for row in grid[r:r + 3]]
            return set(x for row in m for x in row) == set(range(1, 10)) \
                   and all(sum(row) == 15 for row in m) \
                   and all(sum(col) == 15 for col in zip(*m)) \
                   and m[2][2] + m[0][0] == 10 \
                   and m[0][2] + m[2][0] == 10

        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        ans = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if grid[i + 1][j + 1] == 5 and isMagic(i, j):
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [[4, 3, 8, 4],
             [9, 5, 1, 9],
             [2, 7, 6, 2]]
            , 1
    ),
    (
            [[3, 2, 9, 2, 7],
             [6, 1, 8, 4, 2],
             [7, 5, 3, 2, 7],
             [2, 9, 4, 9, 6],
             [4, 3, 8, 2, 5]]
            , 1),
])
def test_solutions(args, expected):
    assert Solution().numMagicSquaresInside(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
