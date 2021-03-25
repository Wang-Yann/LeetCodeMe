#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-01-19 02:21:18
# @Last Modified : 2021-01-19 02:21:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。 
# 
#  连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 
# val 的绝对值。 
# 
#  请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
# 
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
#  
# 
#  示例 2： 
# 
#  
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
#  
# 
#  示例 3： 
# 
#  
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
#  
# 
#  示例 4： 
# 
#  
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
#  
# 
#  示例 5： 
# 
#  
# 输入：points = [[0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 1000 
#  -106 <= xi, yi <= 106 
#  所有点 (xi, yi) 两两不同。 
#  
#  Related Topics 并查集 
#  👍 51 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = lambda x, y: abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])

        N = len(points)
        dsu = UnionFind(N)
        edges = list()

        for i in range(N):
            for j in range(i + 1, N):
                edges.append((dist(i, j), i, j))

        edges.sort()

        ret, num = 0, 1
        for dst, x, y in edges:
            if dsu.union_set(x, y):
                ret += dst
                num += 1
                if num == N:
                    break

        return ret


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20),
    (dict(points=[[3, 12], [-2, 5], [-4, 1]]), 18),
    (dict(points=[[0, 0], [1, 1], [1, 0], [-1, 1]]), 4),
    (dict(points=[[-1000000, -1000000], [1000000, 1000000]]), 4000000),
    (dict(points=[[0, 0]]), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().minCostConnectPoints(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
