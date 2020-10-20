#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 19:03:40
# @Last Modified : 2020-04-21 19:03:40
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
#  例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
#  计算从根到叶子节点生成的所有数字之和。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例 1:
#
#  输入: [1,2,3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
#
#  示例 2:
#
#  输入: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
#  Related Topics 树 深度优先搜索
#  👍 155 👎 0
import functools

import pytest

from common_utils import TreeNode


class Solution0:
    def sumNumbers(self, root: TreeNode) -> int:
        results = []

        def dfs(path, cur):
            if not cur:
                return
            cur_val = cur.val
            if not cur.left and not cur.right:
                path = path * 10 + cur_val
                results.append(path)
                return
            path = path * 10 + cur_val
            dfs(path, cur.left)
            dfs(path, cur.right)
            path //= 10

        dfs(0, root)
        # print(results)
        return sum(results, 0)


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        @functools.lru_cache(None)
        def helper(node, path_sum):
            if not node: return 0
            if not node.left and not node.right:
                return path_sum * 10 + node.val
            return helper(node.left, path_sum * 10 + node.val) \
                   + helper(node.right, path_sum * 10 + node.val)

        return helper(root, 0)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(1, TreeNode(2, ), TreeNode(3))
    ), 25],
    [dict(
        root=TreeNode(
            4,
            left=TreeNode(9, TreeNode(5), TreeNode(1)),
            right=TreeNode(0)
        )
    ), 1026],
])
def test_solutions(kw, expected):
    assert Solution().sumNumbers(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
