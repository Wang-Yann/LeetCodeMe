#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 16:51:46
# @Last Modified : 2020-04-22 16:51:46
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 计算给定二叉树的所有左叶子之和。
#
#  示例：
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
#
#  Related Topics 树
#  👍 166 👎 0

from common_utils import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        stack = [(root, False)]
        res = 0
        while stack:
            cur, is_left = stack.pop()
            if is_left and not cur.left and not cur.right:
                res += cur.val
            if cur.left:
                stack.append((cur.left, True))
            if cur.right:
                stack.append((cur.right, False))

        return res


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(3,
                 left=TreeNode(9),
                 right=TreeNode(20, TreeNode(15), TreeNode(7))),
        TreeNode(9)

    ]
    lists = [x for x in samples]
    res = [sol.sumOfLeftLeaves(x) for x in lists]
    print(res)
