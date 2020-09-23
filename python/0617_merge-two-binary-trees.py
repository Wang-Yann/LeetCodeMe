#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 18:18:46
# @Last Modified : 2020-04-23 18:18:46
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
#  你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点
# 。
#
#  示例 1:
#
#
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
#
#
#  注意: 合并必须从两个树的根节点开始。
#  Related Topics 树
#  👍 419 👎 0

import pytest

from common_utils import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t = TreeNode(t1.val + t2.val)
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)
        return t


@pytest.mark.parametrize("kw,expected", [
    [dict(
        t1=TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)),
        t2=TreeNode(2, TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(7)))
    ), ['3', '4', '5', '5', '4', '#', '7']],
])
def test_solutions(kw, expected):
    res = Solution().mergeTrees(**kw)
    assert repr(res) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
