#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 14:27:02
# @Last Modified : 2020-04-24 14:27:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        elif root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [TreeNode(3, TreeNode(0, right=TreeNode(2, TreeNode(1))), TreeNode(4)),
         1, 3],
        [TreeNode(1, TreeNode(0), TreeNode(2)), 1, 2]

    ]
    lists = [x for x in samples]
    res = [sol.trimBST(*x) for x in lists]
    print(res)
