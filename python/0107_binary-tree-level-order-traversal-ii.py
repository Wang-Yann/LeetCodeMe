#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
#  例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其自底向上的层次遍历为：
#
#  [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 266 👎 0

from collections import deque
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        def levelOrderTraversalRecursive(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                levelOrderTraversalRecursive(node.left, level + 1)
            if node.right:
                levelOrderTraversalRecursive(node.right, level + 1)

        levelOrderTraversalRecursive(root, 0)
        return res[::-1]


class Solution1:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        dq = deque([root])
        while dq:
            level_length = len(dq)
            tmp = []
            for i in range(level_length):
                node = dq.popleft()
                tmp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            levels.insert(0, tmp)

        return levels


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7)),
        )
    ), [[15, 7], [9, 20], [3]]],
])
def test_solutions(kw, expected):
    assert Solution().levelOrderBottom(**kw) == expected
    assert Solution1().levelOrderBottom(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
