#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。 
# 
#  每个人都可能不喜欢其他人，那么他们不应该属于同一组。 
# 
#  形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。 
# 
#  当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
#  
# 
#  示例 2： 
# 
#  输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 2000 
#  0 <= dislikes.length <= 10000 
#  1 <= dislikes[i][j] <= N 
#  dislikes[i][0] < dislikes[i][1] 
#  对于 dislikes[i] == dislikes[j] 不存在 i != j 
#  
#  Related Topics 深度优先搜索

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for src, dest in dislikes:
            graph[src - 1].append(dest - 1)
            graph[dest - 1].append(src - 1)
        color = [0] * N
        for idx, v in enumerate(color):
            if v != 0:
                continue
            q = collections.deque([idx])
            color[0] = 1
            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if color[nei] == color[cur]:
                        return False
                    elif color[nei] == -color[cur]:
                        continue
                    color[nei] = -color[cur]
                    q.append(nei)
        return True


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for src, dest in dislikes:
            graph[src].append(dest)
            graph[dest].append(src)
        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            for neighbor in graph[node]:
                if not dfs(neighbor, c ^ 1):
                    return False
            return True

        for node in range(1, N + 1):
            if node not in color:
                if not dfs(node, 0):
                    return False
        return True


@pytest.mark.parametrize("kwargs,expected", [
    (dict(N=4, dislikes=[[1, 2], [1, 3], [2, 4]]), True),
    (dict(N=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]), False),
    pytest.param(dict(N=3, dislikes=[[1, 2], [1, 3], [2, 3]]), False),
    # 有环 的情况  sublime text ans wrong
    pytest.param(dict(N=5, dislikes=[[1, 2], [3, 4], [4, 5], [3, 5]]), False),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().possibleBipartition(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
