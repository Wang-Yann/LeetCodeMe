#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 18:13:19
# @Last Modified : 2020-04-20 18:13:19
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
#
#
#
#  示例：
#
#  输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
#
#
#  提示：
#
#
#  0 <= n <= 8
#
#  Related Topics 树 动态规划
#  👍 467 👎 0
from typing import List

import pytest

from common_utils import TreeNode


class Solution0:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(last, first=1):
            return [TreeNode(root, left, right)
                    for root in range(first, last + 1)
                    for left in helper(root - 1, first)
                    for right in helper(last, root + 1)] or [None]

        if not n:
            return []
        return helper(n)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        TODO
        """

        def generateTreesRecursive(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                # all possible left subtrees if i is choosen to be a root
                left_trees = generateTreesRecursive(start, i - 1)
                # all possible right subtrees if i is choosen to be a root
                right_trees = generateTreesRecursive(i + 1, end)
                # connect left and right subtrees to the root i
                for l_tree in left_trees:
                    for r_tree in right_trees:
                        current = TreeNode(i)
                        current.left = l_tree
                        current.right = r_tree
                        all_trees.append(current)
            return all_trees

        if not n:
            return []
        return generateTreesRecursive(1, n)


@pytest.mark.parametrize("args,expected", [
    (3, [
        TreeNode(1, right=TreeNode(3, left=TreeNode(2))),
        TreeNode(3, left=TreeNode(2, left=TreeNode(1))),
        TreeNode(3, left=TreeNode(1, right=TreeNode(2))),
        TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
        TreeNode(1, right=TreeNode(2, right=TreeNode(3))),

    ]),
    (0, [])
])
@pytest.mark.parametrize("SolutionCls", [Solution, Solution0])
def test_solutions(args, expected, SolutionCls):
    res = SolutionCls().generateTrees(args)
    res_show = list(map(repr, res))
    expected_show = list(map(repr, expected))
    assert sorted(res_show) == sorted(expected_show)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
