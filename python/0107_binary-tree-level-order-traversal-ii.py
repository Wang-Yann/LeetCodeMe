#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from collections import deque
from typing import List

from common_utils import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        def levelOrderTraversalRecursive(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                levelOrderTraversalRecursive(node.left, level + 1)
            if node.right:
                levelOrderTraversalRecursive(node.right, level + 1)


        levelOrderTraversalRecursive(root, 0)
        return res[::-1]

    def levelOrderBottomBFS(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels
        dq = deque([root])
        while dq:
            level_length = len(dq)
            tmp = []
            for i in range(level_length):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            levels.insert(0, tmp)

        return levels


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.levelOrderBottom(x) for x in lists]
    print(res)
