#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 11:06:04
# @Last Modified : 2020-04-24 11:06:04
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getWidth(root):
            if not root: return 0
            return 2 * max(getWidth(root.left), getWidth(root.right)) + 1

        def getHeight(root):
            if not root: return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1

        def preorderTraversal(root, level, left, right):
            if not root: return
            mid = (left + right) >> 1
            result[level][mid] = str(root.val)
            preorderTraversal(root.left, level + 1, left, mid - 1)
            preorderTraversal(root.right, level + 1, mid + 1, right)

        h, w = getHeight(root), getWidth(root)
        result = [[""] * w for _ in range(h)]
        preorderTraversal(root, 0, 0, w - 1)
        return result


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, TreeNode(2)),
        TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3)),
        None

    ]
    lists = [x for x in samples]
    res = [sol.printTree(x) for x in lists]
    print(res)
