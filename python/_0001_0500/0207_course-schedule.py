#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。 
# 
#  在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1] 
# 
#  给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。 
# 
#  示例 2: 
# 
#  输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。 
# 
#  
# 
#  提示： 
# 
#  
#  输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。 
#  你可以假定输入的先决条件中没有重复的边。 
#  1 <= numCourses <= 10^5 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        拓扑排序
        """
        indegrees = [0] * numCourses
        G = collections.defaultdict(list)
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            G[pre].append(cur)
        # Get all the courses with the indegree of 0.
        dq = collections.deque([i for i in range(numCourses) if indegrees[i] == 0])
        while dq:
            pre = dq.popleft()
            numCourses -= 1
            for cur in G[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    dq.append(cur)
        return numCourses == 0


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """DFS"""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node, visited):
            for j in G[node]:
                if visited[j]:
                    return False
                visited[j] = True
                if not dfs(j, visited):
                    return False
                visited[j] = False
            return True

        G = collections.defaultdict(list)
        for cur, pre in prerequisites:
            G[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, [False] * numCourses):
                return False
        return True


@pytest.mark.parametrize("args,expected", [
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
])
def test_solutions(args, expected):
    assert Solution().canFinish(*args) == expected
    assert Solution1().canFinish(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
