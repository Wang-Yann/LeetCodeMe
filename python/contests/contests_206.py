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


# 1
class Solution1:

    def numSpecial(self, mat: List[List[int]]) -> int:
        ones = []
        one_rows = collections.Counter()
        one_cols = collections.Counter()
        for r, row in enumerate(mat):
            for c, v in enumerate(row):
                if v == 1:
                    ones.append((r, c))
                    one_rows[r] += 1
                    one_cols[c] += 1
        ans = 0
        for x, y in ones:
            if one_rows[x] == one_cols[y] == 1:
                ans += 1
        return ans


@pytest.mark.skip
@pytest.mark.parametrize(
    "kwargs,expected", [
        [
            dict(
                mat=[[1, 0, 0],
                     [0, 0, 1],
                     [1, 0, 0]]), 1],
        [
            dict(
                mat=[[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]]), 3],
        [
            dict(
                mat=[[0, 0, 0, 1],
                     [1, 0, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 0, 0]]), 2],
        [
            dict(
                mat=[[0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 0, 1, 1]]), 3],
    ])
def test_solutions1(kwargs, expected):
    assert Solution1().numSpecial(**kwargs) == expected


# 2
class Solution2:

    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # TODO 真没想出来 就这么暴力过?
        lookup = []
        for pt in preferences:
            lookup.append({t: i for i, t in enumerate(pt)})

        not_happy = set()
        for i, (x, y) in enumerate(pairs):
            for j in range(i + 1, len(pairs)):
                u, v = pairs[j]
                uv, vu = lookup[u][v], lookup[v][u]
                if lookup[x][u] < lookup[x][y] and lookup[u][x] < uv:
                    not_happy.add(x)
                    not_happy.add(u)
                if lookup[x][v] < lookup[x][y] and lookup[v][x] < vu:
                    not_happy.add(x)
                    not_happy.add(v)
                if lookup[y][u] < lookup[y][x] and lookup[u][y] < uv:
                    not_happy.add(y)
                    not_happy.add(u)
                if lookup[y][v] < lookup[y][x] and lookup[v][y] < vu:
                    not_happy.add(y)
                    not_happy.add(v)
        # print(not_happy)
        return len(not_happy)


@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=4, preferences=[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs=[[0, 1], [2, 3]]), 2],
    [dict(n=2, preferences=[[1], [0]], pairs=[[1, 0]]), 0],
    [dict(n=4, preferences=[[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs=[[1, 3], [0, 2]]), 4], ])
def test_solutions2(kwargs, expected):
    assert Solution2().unhappyFriends(**kwargs) == expected


# 3
class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))
        self.size = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        self.size -= 1
        return True


class Solution3:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        N = len(points)
        uf = UnionFind(N + 1)
        costs = []
        for i in range(N):
            for j in range(i + 1, N):
                c = manhattan(points[i], points[j])
                costs.append((c, i, j))
                costs.append((c, j, i))
        res = 0
        for c, x, y in sorted(costs):
            if uf.union_set(x, y):
                res += c
            if uf.size == 1:
                break
        return res


#
@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [

    [dict(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20],
    [dict(points=[[3, 12], [-2, 5], [-4, 1]]), 18],
    [dict(points=[[0, 0], [1, 1], [1, 0], [-1, 1]]), 4],
    [dict(points=[[-1000000, -1000000], [1000000, 1000000]]), 4000000],
    [dict(points=[[0, 0]]), 0],

])
def test_solutions3(kwargs, expected):
    assert Solution3().minCostConnectPoints(**kwargs) == expected


# 4


class Solution4:

    def isTransformable(self, s: str, t: str) -> bool:
        """好理解"""

        if sorted(s) != sorted(t):
            return False
        nxt = collections.defaultdict(collections.deque)
        for i, char in enumerate(s):
            digit = int(char)
            nxt[digit].append(i)

        # print(nxt)
        for char in t:
            digit = int(char)
            limit = nxt[digit].popleft()
            for i in range(digit):
                if nxt[i] and nxt[i][0] < limit:
                    return False
        return True


# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="14234", t="12344"), True],
    [dict(s="84532", t="34852"), True],
    [dict(s="34521", t="23415"), True],
    [dict(s="12345", t="12435"), False],
    [dict(s="1", t="2"), False],
    [dict(s="2", t="1"), False],
    [dict(s="54312", t="21345"), False],
])
def test_solutions4(kwargs, expected):
    assert Solution4().isTransformable(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
