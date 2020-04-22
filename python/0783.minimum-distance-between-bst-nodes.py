#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 22:09:57
# @Last Modified : 2020-04-22 22:09:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:
        prev = float('-inf')
        ans = float('inf')

        def inOrderTraversal(node):
            nonlocal prev, ans
            if node:
                inOrderTraversal(node.left)
                ans = min(ans, node.val - prev)
                prev = node.val
                inOrderTraversal(node.right)

        inOrderTraversal(root)
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, right=TreeNode(3, TreeNode(2))),
        TreeNode(12),
        None
    ]
    res = [sol.minDiffInBST(x) for x in samples]
    print(res)
