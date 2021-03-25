#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:29:30
# @Last Modified : 2020-04-24 16:29:30
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。
#
#  注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
#
#  例如,
#
#
# 给定二叉搜索树:
#
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# 和 插入的值: 5
#
#
#  你可以返回这个二叉搜索树:
#
#
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
#
#
#  或者这个树也是有效的:
#
#
#          5
#        /   \
#       2     7
#      / \
#     1   3
#          \
#           4
#
#  Related Topics 树
#  👍 71 👎 0
import copy

import pytest

from common_utils import TreeNode


class Solution0:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root: return node
        pre, cur = None, root
        while cur:
            if cur.val > val:
                pre, cur = cur, cur.left
            elif cur.val < val:
                pre, cur = cur, cur.right
            else:
                break
        if val <= pre.val:
            node.left = pre.left
            pre.left = node
        else:
            node.right = pre.right
            pre.right = node
        return root


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root: return node
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(4,
                        TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(7)),
          val=5),
     ['4', '2', '7', '1', '3', '5']],
])
def test_solutions(kw, expected):
    assert repr(Solution().insertIntoBST(**copy.deepcopy(kw))) == repr(expected)
    assert repr(Solution0().insertIntoBST(**copy.deepcopy(kw))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
