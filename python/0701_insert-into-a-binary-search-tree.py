#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:29:30
# @Last Modified : 2020-04-24 16:29:30
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution0:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root: return node
        pre, cur = None, root
        while cur:
            if cur.val > val:
                pre, cur = cur, cur.left
            elif cur.val < val:
                pre, cur = cur, cur.right
            else:
                break
        if val <= pre.val:
            node.left = pre.left
            pre.left = node
        else:
            node.right = pre.right
            pre.right = node
        return root


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root: return node
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5]

    ]
    lists = [x for x in samples]
    res = [sol.insertIntoBST(*x) for x in lists]
    print(res)
