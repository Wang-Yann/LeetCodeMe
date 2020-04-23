#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 14:30:23
# @Last Modified : 2020-04-23 14:30:23
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    """
    TODO
    """

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def heightHelper(root, diameter):
            if not root: return 0, diameter
            left, diameter = heightHelper(root.left, diameter)
            right, diameter = heightHelper(root.right, diameter)
            return 1 + max(left, right), max(diameter, left + right)

        return heightHelper(root, 0)[1]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(1, left=TreeNode(2, right=TreeNode(3, right=TreeNode(9))))
    ]
    lists = [x for x in samples]
    res = [sol.diameterOfBinaryTree(x) for x in lists]
    print(res)
