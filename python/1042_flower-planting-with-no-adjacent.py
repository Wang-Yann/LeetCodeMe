#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有 N 个花园，按从 1 到 N 标记。在每个花园中，你打算种下四种花之一。 
# 
#  paths[i] = [x, y] 描述了花园 x 到花园 y 的双向路径。 
# 
#  另外，没有花园有 3 条以上的路径可以进入或者离开。 
# 
#  你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。 
# 
#  以数组形式返回选择的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用 1, 2, 3, 4 表
# 示。保证存在答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：N = 3, paths = [[1,2],[2,3],[3,1]]
# 输出：[1,2,3]
#  
# 
#  示例 2： 
# 
#  输入：N = 4, paths = [[1,2],[3,4]]
# 输出：[1,2,1,2]
#  
# 
#  示例 3： 
# 
#  输入：N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# 输出：[1,2,3,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10000 
#  0 <= paths.size <= 20000 
#  不存在花园有 4 条或者更多路径可以进入或离开。 
#  保证存在答案。 
#  
#  Related Topics 图

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for s, e in paths:
            graph[s - 1].append(e - 1)
            graph[e - 1].append(s - 1)
        res = [0] * N
        for i in range(N):
            used_colors = []
            for neighbor in graph[i]:
                used_colors.append(res[neighbor])
            # print(used_colors)
            # checking if seen or not seen, if seen, what is color? because its other neighbor will have other color
            for color in range(1, 5):
                if color not in used_colors:
                    res[i] = color
        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        G = [[] for _ in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(N=3, paths=[[1, 2], [2, 3], [3, 1]]), [1, 2, 3]),
    pytest.param(dict(N=4, paths=[[1, 2], [3, 4]]), [1, 2, 1, 2]),
    pytest.param(dict(N=4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]), [1, 2, 3, 4]),
])
def test_solutions(kwargs, expected):
    res = Solution().gardenNoAdj(**kwargs)
    res1 = Solution1().gardenNoAdj(**kwargs)
    assert list(collections.Counter(res).values()) == list(collections.Counter(expected).values())
    assert res1 == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
