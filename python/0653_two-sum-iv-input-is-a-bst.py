#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:04:34
# @Last Modified : 2020-04-23 23:04:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        stack = [root]
        num_set = set()
        while stack:
            node = stack.pop()
            node_val = node.val
            if k - node_val in num_set:
                return True
            num_set.add(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, right=TreeNode(7))), 9]
    ]
    res = [sol.findTarget(*args) for args in samples]
    print(res)
