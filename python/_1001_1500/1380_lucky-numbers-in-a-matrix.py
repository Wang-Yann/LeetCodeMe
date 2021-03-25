#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-08 00:02:14
# @Last Modified : 2020-07-08 00:02:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。 
# 
#  幸运数是指矩阵中满足同时下列两个条件的元素： 
# 
#  
#  在同一行的所有元素中最小 
#  在同一列的所有元素中最大 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
# 输出：[15]
# 解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# 输出：[12]
# 解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
#  
# 
#  示例 3： 
# 
#  输入：matrix = [[7,8],[1,2]]
# 输出：[7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= n, m <= 50 
#  1 <= matrix[i][j] <= 10^5 
#  矩阵中的所有元素都是不同的 
#  
#  Related Topics 数组 
#  👍 16 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = tuple(map(min, matrix))
        cols =  tuple(map(max, zip(*matrix)))
        return [cell for i, row in enumerate(matrix)
                for j, cell in enumerate(row) if rows[i] == cols[j]]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            min_val = min(row)
            c = row.index(min_val)
            if all(matrix[r][c] <= min_val for r in range(m)):
                ans.append(min_val)
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    [dict(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]), [15]],

    pytest.param(dict(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]), [12]),
    pytest.param(dict(matrix=[[7, 8], [1, 2]]), [7]),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().luckyNumbers(**kwargs)) == sorted(expected)
    assert sorted(Solution1().luckyNumbers(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
