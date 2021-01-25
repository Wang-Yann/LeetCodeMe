#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。 
# 
#  （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。 
# 
#  返回区域的数目。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：
# [
#  " /",
#  "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
#  
# 
#  示例 2： 
# 
#  输入：
# [
#  " /",
#  "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
#  
# 
#  示例 3： 
# 
#  输入：
# [
#  "\\/",
#  "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
#  
# 
#  示例 4： 
# 
#  输入：
# [
#  "/\\",
#  "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
#  
# 
#  示例 5： 
# 
#  输入：
# [
#  "//",
#  "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length == grid[0].length <= 30 
#  grid[i][j] 是 '/'、'\'、或 ' '。 
#  
#  Related Topics 深度优先搜索 并查集 图

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        """
        提供一个巧妙的思路。将 / 转为
            001
            010
            100.
            
            空格转为
            000
            000
            000

            \转为
            100
            010
            001。
        将原来n*n方格转为3n * 3n 方格。求0的连通量个数
        """

        def dfs(i, j):
            if 0 <= i <= R - 1 and 0 <= j <= C - 1 and not new_grid[i][j]:
                new_grid[i][j] = 2
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        m, n = len(grid), len(grid[0])
        new_grid = [[0] * 3 * n for _ in range(3 * m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "\\":
                    new_grid[3 * i + 2][3 * j + 2] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i][3 * j] = 1
                elif grid[i][j] == "/":
                    new_grid[3 * i][3 * j + 2] = 1
                    new_grid[3 * i + 1][3 * j + 1] = 1
                    new_grid[3 * i + 2][3 * j] = 1
        R, C = 3 * m, 3 * n

        ans = 0
        for i in range(R):
            for j in range(C):
                if new_grid[i][j] == 0:
                    dfs(i, j)
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([" /", "/ "], 2),
    ([" /", "  "], 1),
    (["\\/", "/\\"], 4),
    (["/\\", "\\/"], 5),
    (["//", "/ "], 3)
])
def test_solutions(args, expected):
    assert Solution().regionsBySlashes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
