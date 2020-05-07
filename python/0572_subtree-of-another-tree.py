#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 15:44:32
# @Last Modified : 2020-04-23 15:44:32
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
"""
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看
# 做它自身的一棵子树。
#
#  示例 1:
# 给定的树 s:
#
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#
#
#  给定的树 t：
#
#
#    4
#   / \
#  1   2
#
#
#  返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
#
#  示例 2:
# 给定的树 s：
#
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#
#
#  给定的树 t：
#
#
#    4
#   / \
#  1   2
#
#
#  返回 false。
#  Related Topics 树

"""

import pytest

from common_utils import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isEqual(cur_s, cur_t):
            if not cur_s and not cur_t: return True
            if not (cur_s and cur_t): return False
            return cur_s.val == cur_t.val \
                   and isEqual(cur_s.left, cur_t.left) \
                   and isEqual(cur_s.right, cur_t.right)

        if not t: return True
        if not s: return False
        stack = [s]
        while stack:
            cur = stack.pop()
            if cur.val == t.val and isEqual(cur, t):
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False


class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and isSame(x.left, y.left) and isSame(x.right, y.right)

        def preOrderTraversal(s, t):
            return s is not None and (
                    isSame(s, t) or preOrderTraversal(s.left, t)
                    or preOrderTraversal(s.right, t)
            )

        return preOrderTraversal(s, t)


@pytest.mark.parametrize("args,expected", [
    [(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
      TreeNode(4, TreeNode(1), TreeNode(2))), True],
    [(TreeNode(3, TreeNode(4, TreeNode(1, TreeNode(1)), TreeNode(2)), TreeNode(5)),
      TreeNode(4, TreeNode(1), TreeNode(2))), False]
])
def test_solutions(args, expected):
    assert Solution().isSubtree(*args) == expected
    assert Solution1().isSubtree(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
