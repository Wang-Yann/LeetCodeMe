#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给一个有 n 个结点的有向无环图，找到所有从 0 到 n-1 的路径并输出（不要求按顺序） 
# 
#  二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点（译者注：有向图是有方向的，即规定了a→b你就不能从b→a）空就是没有下一个
# 结点了。 
# 
#  示例:
# 输入: [[1,2], [3], [3], []] 
# 输出: [[0,1,3],[0,2,3]] 
# 解释: 图是这样的:
# 0--->1
# |    |
# v    v
# 2--->3
# 这有两条路: 0 -> 1 -> 3 和 0 -> 2 -> 3.
#  
# 
#  提示: 
# 
#  
#  结点的数量会在范围 [2, 15] 内。 
#  你可以把路径以任意顺序输出，但在路径内的结点的顺序必须保证。 
#  
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        length = len(graph)
        if not length:
            return []
        ans = []
        origin = 0

        def dfs(path, node, ):
            if node == length - 1:
                ans.append(path[:])
            for neighbor in graph[node]:
                dfs(path + [neighbor], neighbor)

        dfs([origin], origin)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
# input_formatted:[[4,3,1],[3,2,4],[3],[4],[]]
# expected_output:[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# code_output:[[0,4],[0,3,4],[0,1,4]]

@pytest.mark.parametrize("args,expected", [
    ([[1, 2], [3], [3], []],
     [[0, 1, 3], [0, 2, 3]]),
    ([[4, 3, 1], [3, 2, 4],
      [3], [4], []],
     [[0, 4], [0, 3, 4], [0, 1, 3, 4],
      [0, 1, 2, 3, 4], [0, 1, 4]]),
])
def test_solutions(args, expected):
    assert sorted(Solution().allPathsSourceTarget(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
