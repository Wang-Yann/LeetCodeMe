#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你现在手里有一份大小为 N x N 的「地图」（网格） grid，上面的每个「区域」（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，
# 请你找出一个海洋区域，这个海洋区域到离它最近的陆地区域的距离是最大的。 
# 
#  我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x
# 1| + |y0 - y1| 。 
# 
#  如果我们的地图上只有陆地或者海洋，请返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释： 
# 海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释： 
# 海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[i][j] 不是 0 就是 1 
#  
#  Related Topics 广度优先搜索 图

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        sources = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    sources.append((i, j))
        if len(sources) == R * C:
            return -1
        dq = collections.deque(sources)
        level = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while dq:
            l = len(dq)
            for _ in range(l):
                x, y = dq.popleft()
                for i, j in directions:
                    nx, ny = x + i, y + j
                    if 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        dq.append((nx, ny))
            level += 1
        return level


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[1, 0, 1],
      [0, 0, 0],
      [1, 0, 1]], 2),
    ([[1, 0, 0],
      [0, 0, 0],
      [0, 0, 0]], 4),
    ([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], -1)
])
def test_solutions(args, expected):
    assert Solution().maxDistance(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
