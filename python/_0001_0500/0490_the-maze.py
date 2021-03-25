#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 15:24:54
# @Last Modified : 2020-07-29 15:24:54
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 由空地和墙组成的迷宫中有一个球。球可以向上下左右四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。 
# 
#  给定球的起始位置，目的地和迷宫，判断球能否在目的地停下。 
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
# 输出: true
# 
# 解析: 一个可能的路径是 : 左 -> 下 -> 左 -> 下 -> 右 -> 下 -> 右。
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
# 输出: false
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
#  👍 44 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """AC"""
        R, C = len(maze), len(maze[0])
        seen = set()
        start, destination = tuple(start), tuple(destination)
        dq = collections.deque()
        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            dq.append((start, d))
        while dq:
            pos, d = dq.popleft()
            if (pos, d) in seen:
                continue
            if pos == destination:
                return True
            seen.add((pos, d))
            x, y = pos
            i, j = d
            while 0 <= x + i <= R - 1 and 0 <= y + j <= C - 1 and maze[x + i][y + j] == 0:
                x += i
                y += j

            dq.append(((x, y), (d[1], d[0])))
            dq.append(((x, y), (-d[1], -d[0])))
        return False


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def hasPath(self, maze, start, destination):
        def neighbors(maze, node):
            for i, j in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                x, y = node
                while 0 <= x + i < len(maze) and 0 <= y + j < len(maze[0]) and not maze[x + i][y + j]:
                    x += i
                    y += j
                yield x, y

        start, destination = tuple(start), tuple(destination)
        queue = collections.deque([start])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            if node == destination:
                return True
            visited.add(node)
            for neighbor in neighbors(maze, node):
                queue.append(neighbor)

        return False


@pytest.mark.parametrize("kw,expected", [
    [dict(
        maze=[[0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0],
              [1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0]],
        start=[0, 4],
        destination=[4, 4]

    ), True],
    [dict(
        maze=[[0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0],
              [1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0]],
        start=[0, 4],
        destination=[3, 2]

    ), False],
])
def test_solutions(kw, expected):
    assert Solution().hasPath(**kw) == expected
    assert Solution1().hasPath(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
