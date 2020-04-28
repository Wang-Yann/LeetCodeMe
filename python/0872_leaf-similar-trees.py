#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 21:25:13
# @Last Modified : 2020-04-24 21:25:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from common_utils import TreeNode


class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def isLeaf(node):
            return node and not node.left and not node.right

        def dfs(node, results):
            if not node:
                return
            if isLeaf(node):
                results.append(node.val)
            dfs(node.left, results)
            dfs(node.right, results)

        res1, res2 = [], []
        dfs(root1, res1)
        dfs(root2, res2)
        # print(res1, res2)
        return res1 == res2


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [TreeNode(1, TreeNode(2)),
         TreeNode(3, TreeNode(4, TreeNode(2)))]
    ]
    res = [sol.leafSimilar(*args) for args in samples]
    print(res)
