#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 19:10:30
# @Last Modified : 2020-04-20 19:10:30
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
#  假设一个二叉搜索树具有如下特征：
#
#
#  节点的左子树只包含小于当前节点的数。
#  节点的右子树只包含大于当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#
#
#  示例 2:
#
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
#  Related Topics 树 深度优先搜索
#  👍 667 👎 0

import pytest

from common_utils import TreeNode, ListNode


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        """
        乍一看，这是一个平凡的问题。只需要遍历整棵树，检查 node.right.val > node.val
        和 node.left.val < node.val 对每个结点是否成立。
        问题是，这种方法并不总是正确。不仅右子结点要大于该节点，整个右子树的元素都应该大于该节点。
        TODO 这里犯过错

        """

        def isValidRecursive(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not isValidRecursive(node.right, val, upper):
                return False
            if not isValidRecursive(node.left, lower, val):
                return False
            return True

        return isValidRecursive(root)


class Solution2(object):

    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True

        return low < root.val  < high \
               and self.isValidBSTRecu(root.left, low, root.val) \
               and self.isValidBSTRecu(root.right, root.val, high)

@pytest.mark.parametrize("args,expected", [
    (TreeNode.initTreeSimple( [2, 1, 3], [(1, 0)], [(1, 2)]), True),
    (TreeNode.initTreeSimple( [1, None, 2, 3], [(2, 3)], [(0, 2)]), False),
    (TreeNode.initTreeSimple( [3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]), False),
])
def test_solutions(args, expected):
    assert Solution().isValidBST(args) == expected
    assert Solution2().isValidBST(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])
