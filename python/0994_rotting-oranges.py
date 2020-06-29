#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在给定的网格中，每个单元格可以有以下三个值之一： 
# 
#  
#  值 0 代表空单元格； 
#  值 1 代表新鲜橘子； 
#  值 2 代表腐烂的橘子。 
#  
# 
#  每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。 
# 
#  返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#  
# 
#  示例 3： 
# 
#  输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 10 
#  1 <= grid[0].length <= 10 
#  grid[i][j] 仅为 0、1 或 2 
#  
#  Related Topics 广度优先搜索

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotted = list()
        good = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotted.append((i, j))
                elif grid[i][j] == 1:
                    good.add((i, j))
        if not good:
            return 0
        ans = 0
        dq = collections.deque(rotted)
        while dq:
            for i in range(len(dq)):
                r, c = dq.popleft()
                for nr, nc in [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]:
                    if 0 <= nr <= m - 1 and 0 <= nc <= n - 1 and (nr, nc) in good:
                        grid[nr][nc] = 2
                        dq.append((nr, nc))
                        good.discard((nr, nc))
            ans += 1
        return ans - 1 if not good else -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 2]], 0),
    ([[0]], 0),
    ([[1], [2], [1], [2]], 1),
])
def test_solutions(args, expected):
    assert Solution().orangesRotting(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
