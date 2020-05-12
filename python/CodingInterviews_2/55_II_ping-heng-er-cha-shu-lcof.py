#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。 
# 
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
# 
#  限制： 
# 
#  
#  1 <= 树的结点个数 <= 10000 
#  
# 
#  注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/ 
# 
#  
#  Related Topics 树 深度优先搜索

"""
import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        """
        PostOrder Traversal Once
        """

        def postOrderTraversal(node):
            if not node:
                return True, 0
            left_res, left_height = postOrderTraversal(node.left)
            if not left_res:
                return False, 0
            right_res, right_height = postOrderTraversal(node.right)
            if not right_res:
                return False, 0
            return abs(left_height - right_height) <= 1, 1 + max(left_height, right_height)

        ans,_ = postOrderTraversal(root)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:

    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(node):
            if not node:
                return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1

        if not root:
            return True
        if abs(getHeight(root.left) - getHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20)), True),
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(1))), True),
])
def test_solutions(args, expected):
    assert Solution().isBalanced(args) == expected
    assert Solution1().isBalanced(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
