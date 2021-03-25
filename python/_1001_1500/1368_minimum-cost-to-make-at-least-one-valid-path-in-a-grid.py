#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 21:57:25
# @Last Modified : 2020-07-05 21:57:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 m x n 的网格图 grid 。 grid 中每个格子都有一个数字，对应着从该格子出发下一步走的方向。 grid[i][j] 中的数字可能为以下
# 几种情况： 
# 
#  
#  1 ，下一步往右走，也就是你会从 grid[i][j] 走到 grid[i][j + 1] 
#  2 ，下一步往左走，也就是你会从 grid[i][j] 走到 grid[i][j - 1] 
#  3 ，下一步往下走，也就是你会从 grid[i][j] 走到 grid[i + 1][j] 
#  4 ，下一步往上走，也就是你会从 grid[i][j] 走到 grid[i - 1][j] 
#  
# 
#  注意网格图中可能会有 无效数字 ，因为它们可能指向 grid 以外的区域。 
# 
#  一开始，你会从最左上角的格子 (0,0) 出发。我们定义一条 有效路径 为从格子 (0,0) 出发，每一步都顺着数字对应方向走，最终在最右下角的格子 (m
#  - 1, n - 1) 结束的路径。有效路径 不需要是最短路径 。 
# 
#  你可以花费 cost = 1 的代价修改一个格子中的数字，但每个格子中的数字 只能修改一次 。 
# 
#  请你返回让网格图至少有一条有效路径的最小代价。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# 输出：3
# 解释：你将从点 (0, 0) 出发。
# 到达 (3, 3) 的路径为： (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 花费代价 cost = 1 使方向向下 --
# > (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 花费代价 cost = 1 使方向向下 --> (2, 0) --> (2,
#  1) --> (2, 2) --> (2, 3) 花费代价 cost = 1 使方向向下 --> (3, 3)
# 总花费为 cost = 3.
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[1,1,3],[3,2,2],[1,1,4]]
# 输出：0
# 解释：不修改任何数字你就可以从 (0, 0) 到达 (2, 2) 。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：grid = [[1,2],[4,3]]
# 输出：1
#  
# 
#  示例 4： 
# 
#  输入：grid = [[2,2,2],[2,2,2]]
# 输出：3
#  
# 
#  示例 5： 
# 
#  输入：grid = [[4]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 100 
#  
#  Related Topics 广度优先搜索 
#  👍 41 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minCost(self, grid: List[List[int]]) -> int:
        """
        Dijsktra
        """
        m, n = len(grid), len(grid[0])
        BIG = 0x7fffffff
        dist = [0] + [BIG] * (m * n - 1)
        seen = set()
        q = [(0, 0, 0)]
        while q:
            cur_dis, x, y = heapq.heappop(q)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            cur_pos = x * n + y
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_pos = nx * n + ny
                new_dis = dist[cur_pos]
                if grid[x][y] != i + 1:
                    new_dis += 1
                if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and new_dis < dist[new_pos]:
                    dist[new_pos] = new_dis
                    heapq.heappush(q, (new_dis, nx, ny))
        return dist[m * n - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]), 3),
    pytest.param(dict(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]]), 0),
    pytest.param(dict(grid=[[1, 2], [4, 3]]), 1),
    pytest.param(dict(grid=[[2, 2, 2], [2, 2, 2]]), 3),
    pytest.param(dict(grid=[[4]]), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().minCost(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
