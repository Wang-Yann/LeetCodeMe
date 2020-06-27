#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。） 
# 
#  现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。 
# 
#  返回必须翻转的 0 的最小数目。（可以保证答案至少是 1。） 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,1],[1,0]]
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：[[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length = A[0].length <= 100 
#  A[i][j] == 0 或 A[i][j] == 1 
#  
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        深度优先搜索，可以得到两座岛的位置集合，分别为 source 和 target。随后我们从 source 中的所有位置开始进行广度优先搜索，
        当它们到达了 target 中的任意一个位置时,即是答案

        """
        R, C = len(A), len(A[0])

        def get_neighbors(r, c):
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr <= R - 1 and 0 <= nc <= C - 1:
                    yield nr, nc

        def get_islands():
            done = set()
            islands = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nx, ny in get_neighbors(*node):
                                if A[nx][ny] and (nx, ny) not in seen:
                                    stack.append((nx, ny))
                                    seen.add((nx, ny))
                        done |= seen
                        islands.append(seen)
            return islands

        source, target = get_islands()
        # print(source, target)
        q = collections.deque([(node, 0) for node in source])
        done = set(source)
        while q:
            node, d = q.popleft()
            if node in target:
                return d - 1
            for nei in get_neighbors(*node):
                if nei not in done:
                    q.append((nei, d + 1))
                    done.add(nei)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [[0, 1],
             [1, 0]]
            , 1),
    pytest.param([[0, 1, 0],
                  [0, 0, 0],
                  [0, 0, 1]], 2),
    pytest.param([[1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 1, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1]], 1),
])
def test_solutions(args, expected):
    assert Solution().shortestBridge(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
