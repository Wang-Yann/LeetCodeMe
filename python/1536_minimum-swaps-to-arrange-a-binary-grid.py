#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 15:05:55
# @Last Modified : 2020-08-09 15:05:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。 
# 
#  一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。 
# 
#  请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。 
# 
#  主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# 输出：-1
# 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length 
#  n == grid[i].length 
#  1 <= n <= 200 
#  grid[i][j] 要么是 0 要么是 1 。 
#  
#  Related Topics 贪心算法 
#  👍 16 👎 0
	 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minSwaps(self, grid: List[List[int]]) -> int:
        """
        1.从第一行开始，如果该行的后缀0满足条件，那么直接跳过进入下一行（因为需要的后缀0个数是从大到小的顺序，所以不必担心前面的会抢后面的）
        2.如果该行后缀0个数不满足条件，那么就往下遍历找到最先（贪心，这是最小次数）满足条件的行，一行一行换上来，
        记录交换的次数（因为题目条件是只能相邻行之间交换，即使换的途中，中间某一行出现了符合的情况，若其上一行不满足后缀0个数，我们还是得移动）
        3.如果找不到满足条件的后缀0，那么就返回-1.


        """
        N = len(grid)
        zeros = [0] * N
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if grid[i][j] == 1:
                    break
            zeros[i] = N - 1 - j
        ans = 0
        for i in range(N - 1):
            if zeros[i] >= N - i - 1:
                continue
            for j in range(i + 1, N):
                if zeros[j] >= N - i - 1:
                    break
            # //找不到，直接返回-1
            else:
                return -1
            for k in range(j, i, -1):
                zeros[k], zeros[k - 1] = zeros[k - 1], zeros[k]
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]]), 3],

    pytest.param(dict(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]), -1),
    pytest.param(dict(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 1]]), 0),
    [dict(grid=[[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]), 2],
    [dict(grid=[[1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0]]), 2],
    [dict(grid=[[1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1]]), 4],

])
def test_solutions(kwargs, expected):
    assert Solution().minSwaps(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
