#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 14:27:02
# @Last Modified : 2020-04-24 14:27:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以
# 结果应当返回修剪好的二叉搜索树的新的根节点。
#
#  示例 1:
#
#
# 输入:
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# 输出:
#     1
#       \
#        2
#
#
#  示例 2:
#
#
# 输入:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# 输出:
#       3
#      /
#    2
#   /
#  1
#
#  Related Topics 树
#  👍 241 👎 0
import pytest

from common_utils import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return root

        elif root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root


@pytest.mark.parametrize("args,expected", [
    ([TreeNode(3, TreeNode(0, right=TreeNode(2, TreeNode(1))), TreeNode(4)),
      1, 3],
     TreeNode(3, TreeNode(2, TreeNode(1)))
     ),
    ([TreeNode(1, TreeNode(0), TreeNode(2)), 1, 2],
     TreeNode(1, None, TreeNode(2))
     )
])
def test_solutions(args, expected):
    assert repr(Solution().trimBST(*args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
