#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 18:18:46
# @Last Modified : 2020-04-23 18:18:46
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        (TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
         TreeNode(2, TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(7))))

    ]
    lists = [x for x in samples]
    res = [sol.mergeTrees(*x) for x in lists]
    print(res)
