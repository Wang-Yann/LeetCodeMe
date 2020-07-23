#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 11:56:48
# @Last Modified : 2020-07-23 11:56:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你是个房地产开发商，想要选择一片空地 建一栋大楼。你想把这栋大楼够造在一个距离周边设施都比较方便的地方，通过调研，你希望从它出发能在 最短的距离和 内抵达周
# 边全部的建筑物。请你计算出这个最佳的选址到周边全部建筑物的 最短距离和。 
# 
#  
# 
#  提示： 
# 
#  你只能通过向上、下、左、右四个方向上移动。 
# 
#  给你一个由 0、1 和 2 组成的二维网格，其中： 
# 
#  
#  0 代表你可以自由通过和选择建造的空地 
#  1 代表你无法通行的建筑物 
#  2 代表你无法通行的障碍物 
#  
# 
#  
# 
#  示例： 
# 
#  输入：[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 输出：7 
# 解析：
# 给定三个建筑物 (0,0)、(0,4) 和 (2,2) 以及一个位于 (0,2) 的障碍物。
# 由于总距离之和 3+3+1=7 最优，所以位置 (1,2) 是符合要求的最优地点，故返回7。
#  
# 
#  
# 
#  注意： 
# 
#  
#  题目数据保证至少存在一栋建筑物，如果无法按照上述规则返回建房地点，则请你返回 -1。 
#  
#  Related Topics 广度优先搜索 
#  👍 29 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        def bfs(i, j):
            visited = [[False] * N for _ in range(M)]
            visited[i][j] = True
            dq = collections.deque([(i, j, 0)])

            while dq:
                i, j, l = dq.popleft()
                if dist[i][j] == float('inf'):
                    dist[i][j] = 0
                dist[i][j] += l

                for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = i + x, j + y
                    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                        visited[nx][ny] = True
                        if grid[nx][ny] == 0:
                            dq.append((nx, ny, l + 1))
                            reachable_count[nx][ny] += 1

        # write your code here
        if not grid:
            return 0
        M, N = len(grid), len(grid[0])

        dist = [[float('inf')] * N for _ in range(M)]
        reachable_count = [[0] * N for _ in range(M)]
        min_dist = float('inf')

        buildings = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    bfs(i, j)
                    buildings += 1
        # print(reachable_count,dist)
        for i in range(M):
            for j in range(N):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]), 7],
])
def test_solutions(kw, expected):
    assert Solution().shortestDistance(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
