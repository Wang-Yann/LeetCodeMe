#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 18:31:01
# @Last Modified : 2020-04-22 18:31:01
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的
# 根节点的引用。
#
#  一般来说，删除节点可分为两个步骤：
#
#
#  首先找到需要删除的节点；
#  如果找到了，删除它。
#
#
#  说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
#  示例:
#
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
#
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
#     5
#    / \
#   2   6
#    \   \
#     4   7
#
#  Related Topics 树
#  👍 235 👎 0
import pytest

from common_utils import TreeNode


class Solution:
    def successor(self, root):
        cur = root.right
        while cur.left:
            cur = cur.left
        return cur.val

    def predecessor(self, root):
        cur = root.left
        while cur.right:
            cur = cur.right
        return cur.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(8,
                        left=TreeNode(1),
                        right=TreeNode(10, TreeNode(9), TreeNode(12))
                        ), key=9),
     TreeNode(8,
              left=TreeNode(1),
              right=TreeNode(10, right=TreeNode(12))
              )
     ],
])
def test_solutions(kw, expected):
    assert repr(Solution().deleteNode(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
