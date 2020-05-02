#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 15:14:49
# @Last Modified : 2020-04-24 15:14:49
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from typing import List




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
