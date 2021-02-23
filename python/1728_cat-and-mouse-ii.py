#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 02:22:17
# @Last Modified : 2021-02-23 02:22:17
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。 
# 
#  它们所处的环境设定是一个 rows x cols 的方格 grid ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。 
# 
#  
#  玩家由字符 'C' （代表猫）和 'M' （代表老鼠）表示。 
#  地板由字符 '.' 表示，玩家可以通过这个格子。 
#  墙用字符 '#' 表示，玩家不能通过这个格子。 
#  食物用字符 'F' 表示，玩家可以通过这个格子。 
#  字符 'C' ， 'M' 和 'F' 在 grid 中都只会出现一次。 
#  
# 
#  猫和老鼠按照如下规则移动： 
# 
#  
#  老鼠 先移动 ，然后两名玩家轮流移动。 
#  每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出 grid 。 
#  catJump 和 mouseJump 是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。 
#  它们可以停留在原地。 
#  老鼠可以跳跃过猫的位置。 
#  
# 
#  游戏有 4 种方式会结束： 
# 
#  
#  如果猫跟老鼠处在相同的位置，那么猫获胜。 
#  如果猫先到达食物，那么猫获胜。 
#  如果老鼠先到达食物，那么老鼠获胜。 
#  如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。 
#  
# 
#  给你 rows x cols 的矩阵 grid 和两个整数 catJump 和 mouseJump ，双方都采取最优策略，如果老鼠获胜，那么请你返回 tr
# ue ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
# 输出：true
# 解释：猫无法抓到老鼠，也没法比老鼠先到达食物。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 4
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = ["M.C...F"], catJump = 1, mouseJump = 3
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 输入：grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
# 输出：false
#  
# 
#  示例 5： 
# 
#  
# 输入：grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 
# 1
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == grid.length 
#  cols = grid[i].length 
#  1 <= rows, cols <= 8 
#  grid[i][j] 只包含字符 'C' ，'M' ，'F' ，'.' 和 '#' 。 
#  grid 中只包含一个 'C' ，'M' 和 'F' 。 
#  1 <= catJump, mouseJump <= 8 
#  
#  Related Topics 动态规划 
#  👍 14 👎 0

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        M, N = len(grid), len(grid[0])
        mouse_pos = cat_pos = None
        available = 0  # available steps for mouse and cat
        # Search the start pos of mouse and cat
        for i in range(M):
            for j in range(N):
                if grid[i][j] != '#':
                    available += 1
                if grid[i][j] == 'M':
                    mouse_pos = (i, j)
                elif grid[i][j] == 'C':
                    cat_pos = (i, j)

        @functools.lru_cache(None)
        def dp(turn, mouse_pos, cat_pos):
            # if turn == m * n * 2:
            # We already search the whole grid (9372 ms 74.3 MB)
            if turn == available * 2:
                # We already search the whole touchable grid (5200 ms 57.5 MB)
                return False
            if turn % 2 == 0:
                # Mouse
                i, j = mouse_pos
                for di, dj in DIRECTIONS:
                    for jump in range(mouseJump + 1):
                        # Note that we want to do range(mouseJump + 1) instead of range(1, mouseJump + 1)
                        # considering the case that we can stay at the same postion for next turn.
                        new_i, new_j = i + di * jump, j + dj * jump
                        if 0 <= new_i < M and 0 <= new_j < N and grid[new_i][new_j] != '#':
                            # Valid pos
                            if dp(turn + 1, (new_i, new_j), cat_pos) or grid[new_i][new_j] == 'F':
                                return True
                        else:
                            # Stop extending the jump since we cannot go further
                            break
                return False
            else:
                # Cat
                i, j = cat_pos
                for di, dj in DIRECTIONS:
                    for jump in range(catJump + 1):
                        new_i, new_j = i + di * jump, j + dj * jump
                        if 0 <= new_i < M and 0 <= new_j < N and grid[new_i][new_j] != '#':
                            if not dp(turn + 1, mouse_pos, (new_i, new_j)) \
                                or (new_i, new_j) == mouse_pos \
                                    or grid[new_i][new_j] == 'F':
                                # This condition will also handle the case that the cat cannot jump through the mouse
                                return False
                        else:
                            break
                return True

        return dp(0, mouse_pos, cat_pos)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(grid=["####F", "#C...", "M...."], catJump=1, mouseJump=2), True],
    [dict(grid=["M.C...F"], catJump=1, mouseJump=4), True],
    [dict(grid=["M.C...F"], catJump=1, mouseJump=3), False],
    [dict(grid=["C...#", "...#F", "....#", "M...."], catJump=2, mouseJump=5), False],
    [dict(grid=[".M...", "..#..", "#..#.", "C#.#.", "...#F"], catJump=3, mouseJump=1), True],
])
def test_solutions(kw, expected):
    assert Solution().canMouseWin(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
