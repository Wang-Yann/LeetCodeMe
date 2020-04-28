#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:12:13
# @Last Modified : 2020-04-23 23:12:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        """TODO"""
        node = TreeNode(val)
        if not root:
            return node
        if val > root.val:
            node.left = root
            return node
        cur = root
        while cur.right and cur.right.val > val:
            cur = cur.right
        cur.right, node.left = node, cur.right
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [TreeNode(4, TreeNode(1), TreeNode(3, TreeNode(2))), 5]

    ]
    res = [sol.insertIntoMaxTree(*args) for args in samples]
    print(res)
