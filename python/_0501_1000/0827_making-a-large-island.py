#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在二维地图上， 0代表海洋， 1代表陆地，我们最多只能将一格 0 海洋变成 1变成陆地。 
# 
#  进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 1 可形成岛屿） 
# 
#  示例 1: 
# 
#  
# 输入: [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
#  
# 
#  示例 2: 
# 
#  
# 输入: [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。 
# 
#  示例 3: 
# 
#  
# 输入: [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。 
# 
#  说明: 
# 
#  
#  1 <= grid.length = grid[0].length <= 50 
#  0 <= grid[i][j] <= 1 
#  
#  Related Topics 深度优先搜索

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, index):
            if not (0 <= r <= ROWS - 1 and 0 <= c <= COLS - 1 and grid[r][c] == 1):
                return 0
            result = 1
            grid[r][c] = index
            for x, y in directions:
                result += dfs(r + x, c + y, index)
            return result

        area = {}
        index = 2
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        result = max(area.values() or [0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    seen = set()
                    for x, y in directions:
                        nr, nc = r + x, c + y
                        if not (0 <= nr <= ROWS - 1 and 0 <= nc <= COLS - 1 and grid[nr][nc] > 1):
                            continue
                        seen.add(grid[nr][nc])
                    result = max(result, 1 + sum(area[i] for i in seen))
        # print("After Area",area)
        return result


# leetcode submit region end(Prohibit modification and deletion)
class SolutionTLE(object):
    """暴力法　超时"""

    def largestIsland(self, grid):
        N = len(grid)

        def check(r, c):
            seen = {(r, c)}
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                    if (nr, nc) not in seen and 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return len(seen)

        ans = 0
        has_zero = False
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    has_zero = True
                    grid[r][c] = 1
                    ans = max(ans, check(r, c))
                    grid[r][c] = 0

        return ans if has_zero else N * N


@pytest.mark.parametrize("args,expected", [
    ([[1, 0], [0, 1]], 3),
    ([[1, 1], [1, 0]], 4),
    ([[1, 1], [1, 1]], 4),
])
def test_solutions(args, expected):
    assert Solution().largestIsland(args) == expected
    assert SolutionTLE().largestIsland(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
