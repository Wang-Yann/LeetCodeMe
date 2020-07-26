#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-26 22:09:25
# @Last Modified : 2020-07-26 22:09:25
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定一个非空01二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。 
# 
#  请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。 
# 
#  
# 
#  样例 1: 
# 
#  11000
# 11000
# 00011
# 00011
#  
# 
#  给定上图，返回结果 1。 
# 
#  
# 
#  样例 2: 
# 
#  11011
# 10000
# 00001
# 11011 
# 
#  给定上图，返回结果 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, m
# onospace">3</font>。 
#  
# 注意: 
# 
#  11
# 1
#  
# 
#  和 
# 
#   1
# 11
#  
# 
#  是不同的岛屿，因为我们不考虑旋转、翻转操作。 
# 
#  
# 
#  注释 : 二维数组每维的大小都不会超过50。 
#  Related Topics 深度优先搜索 哈希表 
#  👍 31 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        问题的关键在于如何描述一个岛屿的形状.
        有以下两个基本思路:

        记录一个岛屿所有点相对于左上角的点的相对位置.
        记录一个岛屿的bfs/dfs轨迹
        方法1涉及细节较少, 但是可能复杂度相对较高, 不过 50x50 的数据范围不会超时.
        方法1也有多种实现方法, 比如一个岛屿形状可以用set记录, 也可以将所有点的相对坐标排序后转换成字符串.

        方法2需要注意一个细节: 不能仅仅储存下来dfs/bfs移动的方向, 因为涉及到回溯等问题, 可以加上一定的间隔符, 或者除方向之外额外记录一个位置信息.



        """
        directions = {'l':[-1, 0], 'r':[1, 0], 'u':[0, 1], 'd':[0, -1]}
        R, C = len(grid), len(grid[0])

        def dfs(i, j, island):
            """
            dfs的路径是一样的，两个图形就是一样的
            """
            if not (0 <= i < R and 0 <= j < C and grid[i][j] > 0):
                return False
            grid[i][j] *= -1
            for k, [x, y] in directions.items():
                island.append(k)
                dfs(i + x, j + y, island)
            return True

        islands = set()
        for i in range(R):
            for j in range(C):
                island = []
                if dfs(i, j, island):
                    islands.add("".join(island))
        # print(islands)
        return len(islands)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]
     ]
    , 1),
    pytest.param([
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],

    ], 3),
])
def test_solutions(args, expected):
    assert Solution().numDistinctIslands(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
