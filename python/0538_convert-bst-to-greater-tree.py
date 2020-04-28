#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 14:17:27
# @Last Modified : 2020-04-23 14:17:27
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution0:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def helper(node, cur_sum):
            if not node:
                return 0
            if node.right:
                cur_sum = helper(node.right, cur_sum)
            cur_sum += node.val
            node.val = cur_sum
            if node.left:
                cur_sum = helper(node.left, cur_sum)
            return cur_sum

        helper(root, 0)
        return root


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """从右向左的中序遍历"""
        cur = root
        stack = []
        total_sum = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            total_sum += cur.val
            cur.val = total_sum
            cur = cur.left
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(5, TreeNode(2), TreeNode(13)),
        None

    ]
    lists = [x for x in samples]
    res = [sol.convertBST(x) for x in lists]
    print(res)
