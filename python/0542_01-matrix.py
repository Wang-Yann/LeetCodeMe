#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 18:26:50
# @Last Modified : 2020-04-15 18:26:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
#
#  两个相邻元素间的距离为 1 。
#
#  示例 1:
# 输入:
#
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#  输出:
#
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#  示例 2:
# 输入:
#
#
# 0 0 0
# 0 1 0
# 1 1 1
#
#
#  输出:
#
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
#  注意:
#
#
#  给定矩阵的元素个数不超过 10000。
#  给定矩阵中至少有一个元素是 0。
#  矩阵中的元素只在四个方向上相邻: 上、下、左、右。
#
#  Related Topics 深度优先搜索 广度优先搜索
#  👍 290 👎 0

import collections
import queue
from typing import List


class Solution(object):

    def updateMatrixS(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:return []
        m, n = len(matrix), len(matrix[0])
        # res = [[0] * n for _ in range(m)]
        q = queue.Queue()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.put((i, j))
                else:
                    matrix[i][j] = float("inf")
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # print(q)
        while not q.empty():
            cell = q.get()
            # print(cell)

            for direct in directions:
                i, j = cell[0] + direct[0], cell[1] + direct[1]
                if not (0 <= i <= m - 1) or not (0 <= j <= n - 1) or matrix[i][j] <= matrix[cell[0]][cell[1]] + 1:
                    continue
                q.put((i, j))
                matrix[i][j] = matrix[cell[0]][cell[1]] + 1
        return matrix

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist



if __name__ == '__main__':
    sol = Solution()
    samples = [
        [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 0, 1, 0, 0]
        ],
        [[0,0,0],[0,1,0],[0,0,0]]
    ]
    # res = [sol.updateMatrix(x) for x in samples]
    res = [sol.updateMatrix(x) for x in samples]
    print(res)
