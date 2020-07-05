#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 16:09:25
# @Last Modified : 2020-07-05 16:09:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。 
# 
#  游戏地图用大小为 n * m 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。 
# 
#  现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ： 
# 
#  
#  玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。 
#  地板用字符 '.' 表示，意味着可以自由行走。 
#  墙用字符 '#' 表示，意味着障碍物，不能通行。 
#  箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。 
#  玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。 
#  玩家无法越过箱子。 
#  
# 
#  返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#             ["#",".",".","B",".","#"],
#             ["#",".","#","#",".","#"],
#             ["#",".",".",".","S","#"],
#             ["#","#","#","#","#","#"]]
# 输出：3
# 解释：我们只需要返回推箱子的次数。 
# 
#  示例 2： 
# 
#  输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#             ["#",".",".","B",".","#"],
#             ["#","#","#","#",".","#"],
#             ["#",".",".",".","S","#"],
#             ["#","#","#","#","#","#"]]
# 输出：-1
#  
# 
#  示例 3： 
# 
#  输入：grid = [["#","#","#","#","#","#"],
#             ["#","T",".",".","#","#"],
#             ["#",".","#","B",".","#"],
#             ["#",".",".",".",".","#"],
#             ["#",".",".",".","S","#"],
#             ["#","#","#","#","#","#"]]
# 输出：5
# 解释：向下、向左、向左、向上再向上。
#  
# 
#  示例 4： 
# 
#  输入：grid = [["#","#","#","#","#","#","#"],
#             ["#","S","#",".","B","T","#"],
#             ["#","#","#","#","#","#","#"]]
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 20 
#  1 <= grid[i].length <= 20 
#  grid 仅包含字符 '.', '#', 'S' , 'T', 以及 'B'。 
#  grid 中 'S', 'B' 和 'T' 各只能出现一个。 
#  
#  Related Topics 广度优先搜索 
#  👍 34 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minPushBox(self, grid: List[List[str]]) -> int:
        """ A* 算法"""
        R, C = len(grid), len(grid[0])
        start_box = target = start_person = None
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "T":
                    target = (i, j)
                elif grid[i][j] == "B":
                    start_box = (i, j)
                elif grid[i][j] == "S":
                    start_person = (i, j)

        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])

        def out_bounds(location):
            """
            # return whether the location is in the grid and not a wall
            """
            r, c = location
            return not (0 <= r <= R - 1 and 0 <= c <= C - 1 and grid[r][c] != "#")

        heap = [[heuristic(start_box), 0, start_person, start_box]]
        visited = set()
        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves
            if (person, box) in visited:
                continue
            visited.add((person, box))

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                new_person = (person[0] + dr, person[1] + dc)
                if out_bounds(new_person):
                    continue
                if new_person == box:
                    new_box = (box[0] + dr, box[1] + dc)
                    if out_bounds(new_box):
                        continue
                    heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box])
        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        grid=[["#", "#", "#", "#", "#", "#"],
              ["#", "T", "#", "#", "#", "#"],
              ["#", ".", ".", "B", ".", "#"],
              ["#", ".", "#", "#", ".", "#"],
              ["#", ".", ".", ".", "S", "#"],
              ["#", "#", "#", "#", "#", "#"]]
    ), 3),
    pytest.param(dict(grid=[["#", "#", "#", "#", "#", "#"],
                            ["#", "T", "#", "#", "#", "#"],
                            ["#", ".", ".", "B", ".", "#"],
                            ["#", "#", "#", "#", ".", "#"],
                            ["#", ".", ".", ".", "S", "#"],
                            ["#", "#", "#", "#", "#", "#"]]), -1),
    pytest.param(dict(grid=[["#", "#", "#", "#", "#", "#"],
                            ["#", "T", ".", ".", "#", "#"],
                            ["#", ".", "#", "B", ".", "#"],
                            ["#", ".", ".", ".", ".", "#"],
                            ["#", ".", ".", ".", "S", "#"],
                            ["#", "#", "#", "#", "#", "#"]]), 5),
    pytest.param(dict(grid=[["#", "#", "#", "#", "#", "#", "#"],
                            ["#", "S", "#", ".", "B", "T", "#"],
                            ["#", "#", "#", "#", "#", "#", "#"]]), -1),
])
def test_solutions(kwargs, expected):
    assert Solution().minPushBox(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
