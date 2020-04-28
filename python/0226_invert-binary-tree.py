#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:39:43
# @Last Modified : 2020-04-22 10:39:43
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def invertTreeMe(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack=[root]
        while stack:
            node  = stack.pop()
            node.left,node.right=node.right,node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9))
        )

    ]
    lists = [x for x in samples]
    print(lists)
    res = [sol.invertTree(x) for x in lists]
    print(res)
