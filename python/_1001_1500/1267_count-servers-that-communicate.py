#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。 
# 
#  如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。 
# 
#  请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[1,0],[0,1]]
# 输出：0
# 解释：没有一台服务器能与其他服务器进行通信。 
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[1,0],[1,1]]
# 输出：3
# 解释：所有这些服务器都至少可以与一台别的服务器进行通信。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# 输出：4
# 解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m <= 250 
#  1 <= n <= 250 
#  grid[i][j] == 0 or 1 
#  
#  Related Topics 图 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        rows_counter = collections.Counter()
        cols_counter = collections.Counter()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    rows_counter[r] += 1
                    cols_counter[c] += 1
        res = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] and (rows_counter[i] > 1 or cols_counter[j] > 1):
                    res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[[1, 0], [0, 1]]), 0],
    [dict(grid=[[1, 0], [1, 1]]), 3],
    [dict(grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), 4],
])
def test_solutions(kw, expected):
    assert Solution().countServers(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
