#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 16:33:21
# @Last Modified : 2020-07-29 16:33:21
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 由空地和墙组成的迷宫中有一个球。球可以向上下左右四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。 
# 
#  给定球的起始位置，目的地和迷宫，找出让球停在目的地的最短距离。距离的定义是球从起始位置（不包括）到目的地（包括）经过的空地个数。如果球无法停在目的地，返回
#  -1。 
# 
#  迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。 
# 
#  
# 
#  示例 1: 
# 
#  输入 1: 迷宫由以下二维数组表示
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# 输入 2: 起始位置坐标 (rowStart, colStart) = (0, 4)
# 输入 3: 目的地坐标 (rowDest, colDest) = (4, 4)
# 
# 输出: 12
# 
# 解析: 一条最短路径 : left -> down -> left -> down -> right -> down -> right。
#              总距离为 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12。
# 
#  
# 
#  示例 2: 
# 
#  输入 1: 迷宫由以下二维数组表示
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# 输入 2: 起始位置坐标 (rowStart, colStart) = (0, 4)
# 输入 3: 目的地坐标 (rowDest, colDest) = (3, 2)
# 
# 输出: -1
# 
# 解析: 没有能够使球停在目的地的路径。
# 
#  
# 
#  
# 
#  注意: 
# 
#  
#  迷宫中只有一个球和一个目的地。 
#  球和目的地都在空地上，且初始时它们不在同一位置。 
#  给定的迷宫不包括边界 (如图中的红色矩形), 但你可以假设迷宫的边缘都是墙壁。 
#  迷宫至少包括2块空地，行数和列数均不超过100。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 32 👎 0

"""

import heapq
from typing import List

import pytest

from sample_datas import BIG_505


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        """
        TODO
        注意和490区别
        Dijkstra+堆优化
        """

        def neighbors(node):
            for i, j in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                x, y = node
                while 0 <= x + i < len(maze) and 0 <= y + j < len(maze[0]) and not maze[x + i][y + j]:
                    x += i
                    y += j
                yield abs(x - node[0]) + abs(y - node[1]), (x, y)

        start, destination = tuple(start), tuple(destination)
        min_heap = [(0, start)]
        visited = set()
        while min_heap:
            cur_dis, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            if node == destination:
                return cur_dis
            visited.add(node)
            for dis, neighbor in neighbors(node):
                heapq.heappush(min_heap, (cur_dis + dis, neighbor))

        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        maze=[[0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0],
              [1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0]],
        start=[0, 4],
        destination=[4, 4]

    ), 12],
    [dict(
        maze=[[0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0],
              [1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0]],
        start=[0, 4],
        destination=[3, 2]

    ), -1],
    [dict(
        maze=BIG_505.BIG_CASE,
        start=[37, 88],
        destination=[60, 33],

    ), 192],
])
def test_solutions(kw, expected):
    assert Solution().shortestDistance(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
