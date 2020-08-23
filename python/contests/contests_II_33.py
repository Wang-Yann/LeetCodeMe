#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-22 20:35:06
# @Last Modified : 2020-08-22 20:35:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
from typing import List

import pytest


# 5479
class Solution1:

    def thousandSeparator(self, n: int) -> str:
        chars = list(str(n))
        ans = ""
        for i, char in enumerate(reversed(chars)):
            ans = char + ans
            if i % 3 == 2:
                ans = "." + ans
        return ans.lstrip(".")


@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=987), "987"],
    [dict(n=0), "0"],
    pytest.param(dict(n=1234), "1.234"),
    pytest.param(dict(n=123456789), "123.456.789"),
])
def test_solutions1(kwargs, expected):
    assert Solution1().thousandSeparator(**kwargs) == expected


# 5480
class Solution2:

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = collections.Counter()
        for s, e in edges:
            indegree[e] += 1
        return list(set(range(n)) - indegree.keys())


@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]), [0, 3]],
    [dict(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]), [0, 2, 3]],
])
def test_solutions2(kwargs, expected):
    assert Solution2().findSmallestSetOfVertices(**kwargs) == expected


# 5481
class Solution3:

    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        while True:
            if all(x == 0 for x in nums):
                break
            if all(x % 2 == 0 for x in nums):
                nums = [x // 2 for x in nums]
                ans += 1
            for i in range(N):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ans += 1
        return ans


#
@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[1, 5]), 5],
    pytest.param(dict(nums=[2, 2]), 3),
    pytest.param(dict(nums=[4, 2, 5]), 6),
    pytest.param(dict(nums=[3, 2, 2, 4]), 7),
    pytest.param(dict(nums=[2, 4, 8, 16]), 8),
    pytest.param(dict(nums=[10 ** 8 + 1, 4, 8, 16]), 42),

])
def test_solutions3(kwargs, expected):
    assert Solution3().minOperations(**kwargs) == expected


# 5482
# class Solution40:
#
#     def containsCycle(self, grid: List[List[str]]) -> bool:
#         """
#         确实没想出好办法
#         TLE
#         70 / 74 个通过测试用例
#         """
#         if not grid:
#             return False
#         R, C = len(grid), len(grid[0])
#         G = collections.defaultdict(set)
#         for i in range(R):
#             for j in range(C):
#                 G[grid[i][j]].add((i, j))
#
#         def dfs(pos, path):
#             if pos == path[0]:
#                 if len(path) >= 4:
#                     return True
#             x, y = pos
#             res = False
#             seen.add(pos)
#             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and grid[nx][ny] == grid[x][y]:
#                     if (nx, ny) not in seen:
#                         res = res or dfs((nx, ny), path + [(nx, ny)])
#                     elif (nx, ny) == path[0]:
#                         res = res or len(path) >= 4
#                 if res:
#                     return True
#             return False
#
#         def get_score(x, y):
#             score = 0
#             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and grid[nx][ny] == grid[x][y]:
#                     score += 1
#             return score
#
#         for i in range(R):
#             for j in range(C):
#                 seen = set()
#                 if len(G[grid[i][j]]) >= 4 and get_score(i, j) == 2:
#                     if dfs((i, j), [(i, j)]):
#                         return True
#
#         return False


class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution4:

    def containsCycle(self, grid: List[List[str]]) -> bool:

        if not grid:
            return False
        R, C = len(grid), len(grid[0])
        uf = UnionFind(R * C)
        for i in range(R):
            for j in range(C):
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.union_set(i * C + j, (i - 1) * C + j):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.union_set(i * C + j, i * C + j - 1):
                        return True
        return False


# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(grid=[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]), True],
    [dict(grid=[["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]), True],
    [dict(grid=[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]), False],
    [dict(grid=[["f", "c", "b", "d", "f", "a", "e", "e", "a", "c", "e"], ["d", "f", "f", "c", "c", "a", "b", "b", "a", "c", "f"],
                ["e", "d", "d", "a", "d", "d", "d", "c", "f", "b", "e"], ["e", "a", "d", "d", "a", "e", "e", "a", "c", "f", "b"],
                ["d", "c", "f", "a", "b", "c", "c", "d", "e", "c", "b"], ["d", "a", "e", "d", "a", "a", "a", "e", "f", "a", "b"],
                ["d", "f", "e", "a", "f", "b", "c", "b", "d", "a", "e"], ["c", "f", "d", "c", "d", "a", "e", "e", "a", "a", "e"],
                ["f", "b", "c", "e", "e", "b", "e", "b", "a", "a", "a"], ["d", "d", "b", "c", "b", "f", "a", "c", "b", "c", "d"],
                ["e", "e", "c", "c", "e", "b", "e", "f", "b", "c", "d"]]), True],
])
def test_solutions4(kwargs, expected):
    assert Solution4().containsCycle(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
