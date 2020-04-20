#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution0:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def preorderTraversalRecursive(node, result):
            if node is None:
                return
            result.append(node.val)
            preorderTraversalRecursive(node.left, result)
            preorderTraversalRecursive(node.right, result)

        preorderTraversalRecursive(root, res)
        return res


class Solution:
    """迭代　基"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)

        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.preorderTraversal(x) for x in lists]
    print(res)
