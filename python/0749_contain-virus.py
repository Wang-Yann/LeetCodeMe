#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。 
# 
#  假设世界由二维矩阵组成，0 表示该区域未感染病毒，而 1 表示该区域已感染病毒。可以在任意 2 个四方向相邻单元之间的共享边界上安装一个防火墙（并且只有一
# 个防火墙）。 
# 
#  每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连
# 续的一片区域），且该感染区域对未感染区域的威胁最大且保证唯一。 
# 
#  你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。 
# 
#  
# 
#  示例 1： 
# 
#  输入: grid = 
# [[0,1,0,0,0,0,0,1],
#  [0,1,0,0,0,0,0,1],
#  [0,0,0,0,0,0,0,1],
#  [0,0,0,0,0,0,0,0]]
# 输出: 10
# 说明:
# 一共有两块被病毒感染的区域: 从左往右第一块需要 5 个防火墙，同时若该区域不隔离，晚上将感染 5 个未感染区域（即被威胁的未感染区域个数为 5）;
# 第二块需要 4 个防火墙，同理被威胁的未感染区域个数是 4。因此，第一天先隔离左边的感染区域，经过一晚后，病毒传播后世界如下:
# [[0,1,0,0,0,0,1,1],
#  [0,1,0,0,0,0,1,1],
#  [0,0,0,0,0,0,1,1],
#  [0,0,0,0,0,0,0,1]]
# 第二题，只剩下一块未隔离的被感染的连续区域，此时需要安装 5 个防火墙，且安装完毕后病毒隔离任务完成。
#  
# 
#  示例 2： 
# 
#  输入: grid = 
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# 输出: 4
# 说明: 
# 此时只需要安装 4 面防火墙，就有一小区域可以幸存，不被病毒感染。
# 注意不需要在世界边界建立防火墙。 
# 
#  
# 
#  示例 3: 
# 
#  输入: grid = 
# [[1,1,1,0,0,0,0,0,0],
#  [1,0,1,0,1,1,1,1,1],
#  [1,1,1,0,0,0,0,0,0]]
# 输出: 13
# 说明: 
# 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙了。
#  
# 
#  
# 
#  说明: 
# 
#  
#  grid 的行数和列数范围是 [1, 50]。 
#  grid[i][j] 只包含 0 或 1 。 
#  题目保证每次选取感染区域进行隔离时，一定存在唯一一个对未感染区域的威胁最大的区域。 
#  
# 
#  
#  Related Topics 深度优先搜索

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        """
        找到所有病毒区域（连续的部分），另外跟踪每个区域的边界（周围未受感染的区域）和该区域的周长。
        对病毒最多的区域进行隔离，计算所需要的防火墙，将其数量添加到答案中。
        剩余的病毒向外感染一个区域
        """
        ROWS, COLS = len(grid), len(grid[0])

        def neighbors(r, c):
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + x, c + y
                if 0 <= nr <= ROWS - 1 and 0 <= nc <= COLS - 1:
                    yield nr, nc

        def dfs(r, c):
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)
                    elif grid[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))
                        perimeters[-1] += 1

        ans = 0
        while True:
            # Find all regions, with associated frontiers and perimeters.
            seen = set()
            regions = []
            frontiers = []
            perimeters = []
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(r, c)
            # If there are no regions left, break.
            if not regions:
                break
            # Add the perimeter of the region which will infect the most squares.
            triage_index = frontiers.index(max(frontiers, key=len))
            ans += perimeters[triage_index]
            # Triage the most infectious region, and spread the rest of the regions.
            for i, reg in enumerate(regions):
                if i == triage_index:
                    for r, c in reg:
                        grid[r][c] = -1
                else:
                    for r, c in reg:
                        for nr, nc in neighbors(r, c):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 1
        # print(grid)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [[0, 1, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0]], 10

    ),
    (
            [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]], 4
    ),
    (
            [[1, 1, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1, 1, 1, 1, 1],
             [1, 1, 1, 0, 0, 0, 0, 0, 0]], 13
    )
])
def test_solutions(args, expected):
    assert Solution().containVirus(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
