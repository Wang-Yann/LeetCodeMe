#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 22:35:15
# @Last Modified : 2020-04-24 22:35:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
# 给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
#
#
#
#  示例 ：
#
#  输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]
#
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9
#
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9
#
#
#
#  提示：
#
#
#  给定树中的结点数介于 1 和 100 之间。
#  每个结点都有一个从 0 到 1000 范围内的唯一整数值。
#
#  Related Topics 树 深度优先搜索
#  👍 83 👎 0
import copy

import pytest

from common_utils import TreeNode


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        cur = root
        stack = []
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        new_root = TreeNode(res[0])
        cur = new_root
        for i in range(1, len(res)):
            cur.right = TreeNode(res[i])
            cur = cur.right
        return new_root


class Solution1:
    """具体地，当我们遍历到一个节点时，把它的左孩子设为空，并将其本身作为上一个遍历到的节点的右孩子。"""

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(cur, pre):
            if not cur:
                return pre
            result = helper(cur.left, cur)
            cur.left = None
            cur.right = helper(cur.right, pre)
            return result

        return helper(root, None)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(5,
                        TreeNode(3, TreeNode(2), TreeNode(4)))
          ),
     ['2', '#', '3', '#', '4', '#', '5']],
])
def test_solutions(kw, expected):
    assert repr(Solution().increasingBST(**copy.deepcopy(kw))) == repr(expected)
    assert repr(Solution1().increasingBST(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
