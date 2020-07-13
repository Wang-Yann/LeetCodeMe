#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:15:03
# @Last Modified : 2020-07-13 11:15:03
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角
# 移动到右下角的路径。 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。 
# 
#  示例 1: 
# 
#  输入:
# [
#  [0,0,0],
#  [0,1,0],
#  [0,0,0]
# ]
# 输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
# 解释: 
# 输入中标粗的位置即为输出表示的路径，即
# 0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角） 
# 
#  说明：r 和 c 的值均不超过 100。 
#  Related Topics 动态规划 
#  👍 24 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        ans, R, C = [], len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1

        def dfs(path):
            if not ans:
                i, j = path[-1]
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 1
                    if j < C: dfs(path + [[i, j + 1]])
                    if i < R: dfs(path + [[i + 1, j]])
                    if i == R and j == C:
                        ans.extend(path)

        dfs([[0, 0]])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]), [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]],
    [dict(obstacleGrid=[[1]]), []],
    [dict(obstacleGrid=[[0]]), [[0, 0]]],
])
def test_solutions(kw, expected):
    assert Solution().pathWithObstacles(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
