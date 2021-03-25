#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 16:50:09
# @Last Modified : 2020-04-21 16:50:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

"""
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
#
#
#  返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#  Related Topics 树 深度优先搜索

"""

import pytest

from common_utils import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if root.val == sum and not root.left and not root.right:
            return True
        res_left, res_right = False, False
        if root.left:
            res_left = self.hasPathSum(root.left, sum - root.val)
        if root.right:
            res_right = self.hasPathSum(root.right, sum - root.val)
        return res_left or res_right

    def hasPathSumSS(self, root: TreeNode, sum: int) -> bool:
        """
        sum - root.val
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val
                               ) or self.hasPathSum(root.right, sum - root.val)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        5,
        left=TreeNode(4, left=TreeNode(11, TreeNode(7), TreeNode(2))),
        right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1)))
    ), sum=22), True],
])
def test_solutions(kw, expected):
    assert Solution().hasPathSum(**kw) == expected
    assert Solution().hasPathSumSS(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
