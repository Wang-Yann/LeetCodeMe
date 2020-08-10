#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 16:50:09
# @Last Modified : 2020-04-21 16:50:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
#
#  返回:
#
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#  Related Topics 树 深度优先搜索
#  👍 274 👎 0


from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    """Me"""

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        results = []

        def dfs(path, cur, sum_val):
            if not cur:
                return
            cur_val = cur.val
            if cur_val == sum_val and not cur.left and not cur.right:
                path.append(cur_val)
                results.append(path)
                return
            dfs(path + [cur_val], cur.left, sum_val - cur.val)
            dfs(path + [cur_val], cur.right, sum_val - cur.val)

        dfs([], root, sum)
        return results


class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        results = []

        def dfs(path, cur, sum_val):
            if not cur:
                return
            cur_val = cur.val
            if cur_val == sum_val and not cur.left and not cur.right:
                results.append(path + [cur_val])
                return
            path.append(cur_val)
            dfs(path, cur.left, sum_val - cur.val)
            dfs(path, cur.right, sum_val - cur.val)
            path.pop()

        dfs([], root, sum)
        return results


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            5,
            left=TreeNode(4, left=TreeNode(11, TreeNode(7), TreeNode(2))),
            right=TreeNode(8,
                           TreeNode(13),
                           TreeNode(4, TreeNode(5), TreeNode(1))
                           ),
        ), sum=22
    ),
        [
            [5, 4, 11, 2],
            [5, 8, 4, 5]
        ]
    ],
])
def test_solutions(kw, expected):
    assert sorted(Solution().pathSum(**kw)) == sorted(expected)
    assert sorted(Solution1().pathSum(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
