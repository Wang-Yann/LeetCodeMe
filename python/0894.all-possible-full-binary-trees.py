#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 22:19:36
# @Last Modified : 2020-04-24 22:19:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution:

    def __init__(self):
        self.possible_map = {1:[TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []

        if N not in self.possible_map:
            results = []
            for i in range(N):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - 1 - i):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        results.append(node)
            self.possible_map[N] = results

        return self.possible_map[N]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        2, 3, 7
    ]
    res = [sol.allPossibleFBT(args) for args in samples]
    print(res)
