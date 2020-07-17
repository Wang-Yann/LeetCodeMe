#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:39:43
# @Last Modified : 2020-04-22 10:39:43
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 翻转一棵二叉树。
#
#  示例：
#
#  输入：
#
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#  输出：
#
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#  备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
#  Related Topics 树
#  👍 500 👎 0

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
