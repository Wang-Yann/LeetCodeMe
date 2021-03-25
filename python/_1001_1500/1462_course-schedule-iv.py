#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 13:49:42
# @Last Modified : 2020-07-10 13:49:42
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你总共需要上 n 门课，课程编号依次为 0 到 n-1 。 
# 
#  有的课会有直接的先修课程，比如如果想上课程 0 ，你必须先上课程 1 ，那么会以 [1,0] 数对的形式给出先修课程数对。 
# 
#  给你课程总数 n 和一个直接先修课程数对列表 prerequisite 和一个查询对列表 queries 。 
# 
#  对于每个查询对 queries[i] ，请判断 queries[i][0] 是否是 queries[i][1] 的先修课程。 
# 
#  请返回一个布尔值列表，列表中每个元素依次分别对应 queries 每个查询对的判断结果。 
# 
#  注意：如果课程 a 是课程 b 的先修课程且课程 b 是课程 c 的先修课程，那么课程 a 也是课程 c 的先修课程。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# 输出：[false,true]
# 解释：课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。
#  
# 
#  示例 2： 
# 
#  输入：n = 2, prerequisites = [], queries = [[1,0],[0,1]]
# 输出：[false,false]
# 解释：没有先修课程对，所以每门课程之间是独立的。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# 输出：[true,true]
#  
# 
#  示例 4： 
# 
#  输入：n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
# 输出：[false,true]
#  
# 
#  示例 5： 
# 
#  输入：n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[
# 1,3],[3,0]]
# 输出：[true,false,true,false]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 100 
#  0 <= prerequisite.length <= (n * (n - 1) / 2) 
#  0 <= prerequisite[i][0], prerequisite[i][1] < n 
#  prerequisite[i][0] != prerequisite[i][1] 
#  先修课程图中没有环。 
#  先修课程图中没有重复的边。 
#  1 <= queries.length <= 10^4 
#  queries[i][0] != queries[i][1] 
#  
#  Related Topics 图 
#  👍 18 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        GOOD TODO
        Floyd–Warshall Algorithm
        O(n**3)
        
        """
        connected = [[False] * n for _ in range(n)]

        for i, j in prerequisites:
            connected[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

        return [connected[i][j] for i, j in queries]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """暴力"""

        def getPre(pre, late):
            dq = collections.deque([pre])
            seen = set()
            while dq:
                node = dq.popleft()
                if node in seen:
                    continue
                seen.add(node)
                for nei in graph[node]:
                    dq.append(nei)
            return late in seen

        graph = collections.defaultdict(list)
        for pre, late in prerequisites:
            graph[pre].append(late)
        ans = []
        for a, b in queries:
            ans.append(getPre(a, b))
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(n=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]), [False, True]],
    [dict(n=2, prerequisites=[], queries=[[1, 0], [0, 1]]), [False, False]],
    [dict(n=3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]), [True, True]],
    [dict(n=3, prerequisites=[[1, 0], [2, 0]], queries=[[0, 1], [2, 0]]), [False, True]],
    [dict(n=5, prerequisites=[[0, 1], [1, 2], [2, 3], [3, 4]], queries=[[0, 4], [4, 0], [1, 3], [3, 0]]),
     [True, False, True, False]],
    [dict(n=5, prerequisites=[[4, 3], [4, 1], [4, 0], [3, 2], [3, 1], [3, 0], [2, 1], [2, 0], [1, 0]],
          queries=[[1, 4], [4, 2], [0, 1], [4, 0], [0, 2], [1, 3], [0, 1]]),
     [False, True, False, True, False, False, False]],
])
def test_solutions(kw, expected):
    assert Solution().checkIfPrerequisite(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
