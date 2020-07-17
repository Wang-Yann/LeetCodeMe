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


import itertools
from typing import List

from common_utils import TreeNode


class Solution:
    def pathSumMe(self, root: TreeNode, sum: int) -> List[List[int]]:
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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]),
        ([1], [], [])

    ]
    sums = [7, 12, 1]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.pathSum(x, y) for x, y in itertools.zip_longest(lists, sums)]
    print(res)
