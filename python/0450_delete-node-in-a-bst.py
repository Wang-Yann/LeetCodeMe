#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 18:31:01
# @Last Modified : 2020-04-22 18:31:01
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def successor(self, root):
        cur = root.right
        while cur.left:
            cur = cur.left
        return cur.val

    def predecessor(self, root):
        cur = root.left
        while cur.right:
            cur = cur.right
        return cur.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root= None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(8,
                 left=TreeNode(1),
                 right=TreeNode(10, TreeNode(9), TreeNode(12))
                 ),
        TreeNode(9),

    ]
    lists = [x for x in samples]
    res = [sol.deleteNode(x, 9) for x in lists]
    print(res)
