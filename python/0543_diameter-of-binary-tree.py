#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 14:30:23
# @Last Modified : 2020-04-23 14:30:23
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
#  示例 :
# 给定二叉树
#
#            1
#          / \
#         2   3
#        / \
#       4   5
#
#
#  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
#  注意：两结点之间的路径长度是以它们之间边的数目表示。
#  Related Topics 树
#  👍 411 👎 0
import pytest

from common_utils import TreeNode


class Solution:
    """
    TODO
    """

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def heightHelper(root, diameter):
            if not root:
                return 0, diameter
            left, diameter = heightHelper(root.left, diameter)
            right, diameter = heightHelper(root.right, diameter)
            return 1 + max(left, right), max(diameter, left + right)

        return heightHelper(root, 0)[1]


@pytest.mark.parametrize("args,expected", [
    [TreeNode(1,
              TreeNode(2, TreeNode(4), TreeNode(5)),
              TreeNode(3)), 3],
    [TreeNode(1,
              TreeNode(2),
              TreeNode(3)), 2],
    [TreeNode(1, left=TreeNode(2, right=TreeNode(3, right=TreeNode(9)))), 3],
])
def test_solutions(args, expected):
    assert Solution().diameterOfBinaryTree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
