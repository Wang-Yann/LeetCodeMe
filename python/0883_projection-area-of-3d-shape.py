#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 23:17:39
# @Last Modified : 2020-05-05 23:17:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def projectionArea(self, grid: List[List[int]]) -> int:
        """
        从顶部看，由该形状生成的阴影将是网格中非零值的数目。
        从侧面看，由该形状生成的阴影将是网格中每一行的最大值。
        从前面看，由该形状生成的阴影将是网格中每一列的最大值。

        例如 [[1,2],[3,4]]：

        顶部的阴影将为 4，因为网格中有四个非零值;
        侧面的阴影为 2 + 4，因为第一行的最大值为 2，第二行的最大值为 4;
        前面的阴影是 3 + 4，因为第一列的最大值是 3，第二列的最大值是 4

        """
        N = len(grid)
        ans = 0
        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]:
                    ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans += best_row + best_col
        return ans


@pytest.mark.parametrize("args,expected", [
    ([[2]], 5),
    ([[1, 0], [0, 2]], 8),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 14),
    ([[2, 2, 2], [2, 1, 2], [2, 2, 2]], 21),
    pytest.param([[1, 2], [3, 4]], 17),
])
def test_solutions(args, expected):
    assert Solution().projectionArea(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
