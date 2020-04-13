#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 22:16:15
# @Last Modified : 2020-04-11 22:16:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from typing import List


class Solution:
    START = 1
    END = 2
    PASS = 0
    NOPASS = -1

    def __init__(self):
        self.must_visit_set = set()
        self.result = []

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        1 表示起始方格。且只有一个起始方格。
        2 表示结束方格，且只有一个结束方格。
        0 表示我们可以走过的空方格。
        -1 表示我们无法跨越的障碍。
        """
        m, n = len(grid), len(grid[0])
        start,end = (0,0),(0,0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.PASS:
                    self.must_visit_set.add((i, j))
                elif grid[i][j]==self.START:
                    start=(i,j)
                    self.must_visit_set.add(start)
                elif grid[i][j]==self.END:
                    end=(i,j)
                    self.must_visit_set.add(end)
        cur_path = [start]
        self.dfs(grid, cur_path, start, m, n)
        return len(self.result)

    def check_point_need_traverse(self, grid,cur_path,cur_pos, m, n):
        return 0 <= cur_pos[0] <= (m - 1) and 0 <= cur_pos[1] <= (n - 1) \
               and grid[cur_pos[0]][cur_pos[1]] not in (self.START, self.NOPASS) \
               and cur_pos not in cur_path

    def dfs(self, grid, cur_path, cur_pos, m, n):
        cur_x, cur_y =cur_pos
        if grid[cur_x][cur_y] == self.END:
            if set(cur_path) == self.must_visit_set:
                self.result.append(cur_path)
        else:
            next_choices = [(cur_x - 1, cur_y), (cur_x + 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]
            for pos in next_choices:
                if self.check_point_need_traverse(grid, cur_path,pos, m, n):
                    self.dfs(grid, cur_path + [pos], pos, m, n)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]],
        # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],
        # [[0, 1], [2, 0]],
        [[1,2]]
    ]
    res = [sol.uniquePathsIII(x) for x in samples]
    print(res)
