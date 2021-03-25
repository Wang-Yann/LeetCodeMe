#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 23:38:23
# @Last Modified : 2020-07-22 23:38:23
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 有一队人（两人或以上）想要在一个地方碰面，他们希望能够最小化他们的总行走距离。 
# 
#  给你一个 2D 网格，其中各个格子内的值要么是 0，要么是 1。 
# 
#  1 表示某个人的家所处的位置。这里，我们将使用 曼哈顿距离 来计算，其中 distance(p1, p2) = |p2.x - p1.x| + |p2.y
#  - p1.y|。 
# 
#  示例： 
# 
#  输入: 
# 
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# 输出: 6 
# 
# 解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
#      (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。 
#  Related Topics 排序 数学 
#  👍 28 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        曼哈顿距离，行列的最佳点分开求，组合起来就是最佳点。 二维->一维。求中位数。

        """
        rows, cols = [], []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        mid = len(rows) // 2
        v1, v2 = rows[mid], cols[mid]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += abs(v1 - i) + abs(v2 - j)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(grid=[
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],

    ]), 6],

])
def test_solutions(kwargs, expected):
    assert Solution().minTotalDistance(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
