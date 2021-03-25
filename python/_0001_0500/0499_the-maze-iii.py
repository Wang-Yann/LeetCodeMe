#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 22:42:04
# @Last Modified : 2020-07-23 22:42:04
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 由空地和墙组成的迷宫中有一个球。球可以向上（u）下（d）左（l）右（r）四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。迷宫中还有
# 一个洞，当球运动经过洞时，就会掉进洞里。 
# 
#  给定球的起始位置，目的地和迷宫，找出让球以最短距离掉进洞里的路径。 距离的定义是球从起始位置（不包括）到目的地（包括）经过的空地个数。通过'u', 'd'
# , 'l' 和 'r'输出球的移动方向。 由于可能有多条最短路径， 请输出字典序最小的路径。如果球无法进入洞，输出"impossible"。 
# 
#  迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。 
# 
#  
# 
#  示例1: 
# 
#  输入 1: 迷宫由以下二维数组表示
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# 输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
# 输入 3: 洞的位置 (rowHole, colHole) = (0, 1)
# 
# 输出: "lul"
# 
# 解析: 有两条让球进洞的最短路径。
# 第一条路径是 左 -> 上 -> 左, 记为 "lul".
# 第二条路径是 上 -> 左, 记为 'ul'.
# 两条路径都具有最短距离6, 但'l' < 'u'，故第一条路径字典序更小。因此输出"lul"。
# 
#  
# 
#  示例 2: 
# 
#  输入 1: 迷宫由以下二维数组表示
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# 输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
# 输入 3: 洞的位置 (rowHole, colHole) = (3, 0)
# 
# 输出: "impossible"
# 
# 示例: 球无法到达洞。
# 
#  
# 
#  
# 
#  注意: 
# 
#  
#  迷宫中只有一个球和一个目的地。 
#  球和洞都在空地上，且初始时它们不在同一位置。 
#  给定的迷宫不包括边界 (如图中的红色矩形), 但你可以假设迷宫的边缘都是墙壁。 
#  迷宫至少包括2块空地，行数和列数均不超过30。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 24 👎 0

"""
import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ball, hole = tuple(ball), tuple(hole)
        DIRS = {'u':(-1, 0), 'r':(0, 1), 'l':(0, -1), 'd':(1, 0)}

        def neighbors(maze, node):
            for dir, vec in DIRS.items():
                cur_node, dist = list(node), 0
                while 0 <= cur_node[0] + vec[0] < len(maze) and \
                        0 <= cur_node[1] + vec[1] < len(maze[0]) and \
                        not maze[cur_node[0] + vec[0]][cur_node[1] + vec[1]]:
                    cur_node[0] += vec[0]
                    cur_node[1] += vec[1]
                    dist += 1
                    if tuple(cur_node) == hole:
                        break
                yield tuple(cur_node), dir, dist

        heap = [(0, '', ball)]
        visited = set()
        while heap:
            dist, path, node = heapq.heappop(heap)
            if node in visited:
                continue
            if node == hole:
                return path
            visited.add(node)
            for neighbor, dir, neighbor_dist in neighbors(maze, node):
                heapq.heappush(heap, (dist + neighbor_dist, path + dir, neighbor))

        return "impossible"


# leetcode submit region end(Prohibit modification and deletion)


class MazeGridType:
    SPACE = 0
    WALL = 1


DIRECTION_HASH = {
    'd':(1, 0),
    'l':(0, -1),
    'r':(0, 1),
    'u':(-1, 0),
}


class Solution1:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """

    def findShortestWay(self, maze, ball, hole):
        hole = (hole[0], hole[1])

        queue = collections.deque([(ball[0], ball[1], '')])
        distance={}
        for d in DIRECTION_HASH:
            distance[(ball[0], ball[1], d)]=0

        while queue:
            x, y, path = queue.popleft()
            if (x, y) == hole:
                return path

            directions = self.get_allowed_directions(x, y, path, maze)
            for d in directions:
                dx, dy = DIRECTION_HASH[d]
                next_x, next_y = x + dx, y + dy

                if self.is_wall(next_x, next_y, maze):
                    continue
                if (next_x, next_y, d) in distance:
                    continue

                if path:
                    distance[(next_x, next_y, d)] = distance[(x, y, path[-1])] + 1
                else:
                    distance[(next_x, next_y, d)] = 1

                new_path = self.get_new_path(path, d)
                queue.append((next_x, next_y, new_path))

        return 'impossible'

    def get_allowed_directions(self, x, y, path, maze):
        if not path:
            return DIRECTION_HASH.keys()

        last_direction = path[-1]
        dx, dy = DIRECTION_HASH[last_direction]
        next_x, next_y = x + dx, y + dy
        if self.is_wall(next_x, next_y, maze):
            return DIRECTION_HASH.keys()

        return [last_direction]

    def get_new_path(self, path, direction):
        if not path:
            return direction
        if path[-1] == direction:
            return path
        return path + direction

    def is_wall(self, x, y, maze):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
            return True
        return maze[x][y] == MazeGridType.WALL


@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        maze=[[0, 0, 0, 0, 0],
              [1, 1, 0, 0, 1],
              [0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1],
              [0, 1, 0, 0, 0], ],
        ball=[4, 3], hole=[0, 1]

    ), "lul"],

    [dict(
        maze=[
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0],
        ],
        ball=[4, 3], hole=[3, 0]

    ), "impossible"],

])
def test_solutions(kwargs, expected):
    assert Solution().findShortestWay(**kwargs) == expected
    assert Solution1().findShortestWay(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
