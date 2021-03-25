#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 
# 
#  graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。 
# 
#  返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：[[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一个可能的路径为 [1,0,2,0,3] 
# 
#  示例 2： 
# 
#  输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一个可能的路径为 [0,1,4,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= graph.length <= 12 
#  0 <= graph[i].length < graph.length 
#  
#  Related Topics 广度优先搜索 动态规划

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        注意题目中的节点个数是 <= 12 的，这是突破口。
        可以使用状态压缩的方式记录有哪些点被访问过了。
        存在 BFS Queue 中的是一个二元组 <visited, stop_at>

        visited 可以理解为是一个 boolean 数组，但是为了更方便查询，我们用二进制的方式来表示 visited。
        也就是说，如果所有点都没有被访问过，visited = 0，如果只访问了标号0和2的点，那么 visited = (101)2 = 5
        每次访问一个新的点只需要让 visited | 1 << node 即可算出新的 visited。
        stop_at 记录的是访问了 visited 这些点以后，停在哪儿了。
        """
        N = len(graph)
        queue = collections.deque([])
        distance = {}
        for x in range(N):
            state = (1 << x, x)
            queue.append(state)
            distance[state] = 0
        while queue:
            visited, stop_at = queue.popleft()
            for neighbor in graph[stop_at]:
                _visited = visited | (1 << neighbor)
                if (_visited, neighbor) in distance:
                    continue
                queue.append((_visited, neighbor))
                distance[_visited, neighbor] = distance[visited, stop_at] + 1
                #GOOD
                if _visited == (1 << N) - 1:
                    # print(distance)
                    return distance[_visited, neighbor]
        return 0


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[1, 2, 3], [0], [0], [0]], 4),
    pytest.param([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4),
])
def test_solutions(args, expected):
    assert Solution().shortestPathLength(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
