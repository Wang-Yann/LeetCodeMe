#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
#  本题中，一棵高度平衡二叉树定义为：
#
#
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
#
#  示例 1:
#
#  给定二叉树 [3,9,20,null,null,15,7]
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回 true 。
#
# 示例 2:
#
#  给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#         1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
#  返回 false 。
#
#
#  Related Topics 树 深度优先搜索
#  👍 377 👎 0
import pytest

from common_utils import TreeNode


class Solution:
    def isBalancedRecursive(self, root: TreeNode) -> bool:

        def height(root):
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1

        if not root: return True

        if abs(height(root.left) - height(root.right)) > 1:
            return False
        return self.isBalancedRecursive(root.left) and self.isBalancedRecursive(root.right)

    def isBalanced(self, root: TreeNode) -> bool:
        """
            # Return whether or not the tree at root is balanced while also returning
            # the tree's height
        """

        def helper(root) -> (bool, int):
            if not root: return True, 0
            left_isbalanced, leftHeight = helper(root.left)
            if not left_isbalanced:
                return False, 0
            right_isbalanced, rightHeight = helper(root.right)
            if not right_isbalanced:
                return False, 0
            return (abs(leftHeight - rightHeight) <= 1), 1 + max(leftHeight, rightHeight)

        return helper(root)[0]



@pytest.mark.parametrize("args,expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20)), True),
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(1))), True),
])
def test_solutions(args, expected):
    assert Solution().isBalanced(args) == expected
    assert Solution().isBalancedRecursive(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
