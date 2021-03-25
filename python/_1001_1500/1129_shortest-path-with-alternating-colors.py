#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。 
# 
#  red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从
# 节点 i 到节点 j 的蓝色有向边。 
# 
#  返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的最短路径的长度，且路径上红色边和蓝色边交替出现。如果不存在这样
# 的路径，那么 answer[x] = -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# 输出：[0,1,-1]
#  
# 
#  示例 2： 
# 
#  输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# 输出：[0,1,-1]
#  
# 
#  示例 3： 
# 
#  输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# 输出：[0,-1,-1]
#  
# 
#  示例 4： 
# 
#  输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# 输出：[0,1,2]
#  
# 
#  示例 5： 
# 
#  输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# 输出：[0,1,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  red_edges.length <= 400 
#  blue_edges.length <= 400 
#  red_edges[i].length == blue_edges[i].length == 2 
#  0 <= red_edges[i][j], blue_edges[i][j] < n 
#  
#  Related Topics 广度优先搜索 图

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = [[[], []] for _ in range(n)]
        for i, j in red_edges:
            graph[i][0].append(j)
        for i, j in blue_edges:
            graph[i][1].append(j)
        INF = 0x7fffffff
        res = [[0, 0]] + [[INF, INF] for _ in range(n - 1)]
        #红 蓝
        bfs = [[0, 0], [0, 1]]
        # print(res)
        for i, c in bfs:
            for j in graph[i][c]:
                if res[j][c] == INF:
                    res[j][c] = res[i][1 ^ c] + 1
                    bfs.append([j, 1 ^ c])
        # print(res)
        return [x if x !=INF else -1 for x in map(min, res)]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]
    ), [0, 1, -1]),
    pytest.param(dict(n=3, red_edges=[[0, 1]], blue_edges=[[2, 1]]), [0, 1, -1]),
    pytest.param(dict(n=3, red_edges=[[1, 0]], blue_edges=[[2, 1]]), [0, -1, -1]),
    pytest.param(dict(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]]), [0, 1, 2]),
    pytest.param(dict(n=3, red_edges=[[0, 1], [0, 2]], blue_edges=[[1, 0]]), [0, 1, 1]),
])
def test_solutions(kwargs, expected):
    assert Solution().shortestAlternatingPaths(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
