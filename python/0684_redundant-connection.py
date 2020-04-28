#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 15:14:49
# @Last Modified : 2020-04-24 15:14:49
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from typing import List


class UnionFind(object):
    def __init__(self, n):
        self.set = list(range(n))

    def find(self, x):
        if self.set[x] != x:
            self.set[x] = self.find(self.set[x])
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root: return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        for s, d in edges:
            if not uf.union_set(s, d):
                return [s, d]
        return []


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [[1, 2], [1, 3], [2, 3]],
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

    ]
    lists = [x for x in samples]
    res = [sol.findRedundantConnection(x) for x in lists]
    print(res)
