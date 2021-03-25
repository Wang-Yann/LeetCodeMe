#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 10:08:29
# @Last Modified : 2020-07-21 10:08:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，要么为空，将此二叉树上下翻转并将它变成一棵树， 原来的右节点将转换成左
# 叶节点。返回新的根。
#
#  例子:
#
#  输入: [1,2,3,4,5]
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# 输出: 返回二叉树的根 [4,5,2,#,#,3,1]
#
#    4
#   / \
#  5   2
#     / \
#    3   1
#
#
#  说明:
#
#  对 [4,5,2,#,#,3,1] 感到困惑? 下面详细介绍请查看 二叉树是如何被序列化的。
#
#  二叉树的序列化遵循层次遍历规则，当没有节点存在时，'#' 表示路径终止符。
#
#  这里有一个例子:
#
#     1
#   / \
#  2   3
#     /
#    4
#     \
#      5
#
#
#  上面的二叉树则被序列化为 [1,2,3,#,#,4,#,#,5].
#  Related Topics 树
#  👍 35 👎 0
import copy

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
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        根据题目描述，树中任何节点的右子节点若存在一定有左子节点，因此思路是向左遍历树进行转化；
        规律是：左子节点变父节点；父节点变右子节点；右子节点变父节点
        """

        def helper(parent, node):
            if not node:
                return parent
            root = helper(node, node.left)
            if parent:
                node.left = parent.right
            else:
                node.left = None
            node.right = parent
            return root

        return helper(None, root)


class Solution1:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        GOOD TODO
        根据题目描述，树中任何节点的右子节点若存在一定有左子节点，因此思路是向左遍历树进行转化；
        规律是：左子节点变父节点；父节点变右子节点；右子节点变父节点
        """
        p, parent, parent_right = root, None, None
        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
        return parent


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(1, left=TreeNode(2, TreeNode(4), TreeNode(5)), right=TreeNode(3)),
     TreeNode(4, left=TreeNode(5), right=TreeNode(2, TreeNode(3), TreeNode(1)))),
])
def test_solutions(args, expected):
    args1 = copy.deepcopy(args)
    res = Solution().upsideDownBinaryTree(args)
    res1 = Solution1().upsideDownBinaryTree(args1)
    assert repr(res) == repr(expected)
    assert repr(res1) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
