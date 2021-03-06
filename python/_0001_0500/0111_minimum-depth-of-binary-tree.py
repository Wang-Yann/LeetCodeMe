#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 14:45:55
# @Last Modified : 2020-04-21 14:45:55
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，找出其最小深度。
#
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例:
#
#  给定二叉树 [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最小深度 2.
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 292 👎 0
import collections

import pytest

from common_utils import TreeNode


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))


class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))), 2],
    [dict(root=TreeNode(1, TreeNode(2))), 2],
])
def test_solutions(kw, expected):
    assert Solution().minDepth(**kw) == expected
    assert Solution1().minDepth(**kw) == expected
    assert Solution2().minDepth(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
