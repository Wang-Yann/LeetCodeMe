#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 16:50:09
# @Last Modified : 2020-04-21 16:50:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个非空二叉树，返回其最大路径和。
#
#  本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
#  示例 1:
#
#  输入: [1,2,3]
#
#        1
#       / \
#      2   3
#
# 输出: 6
#
#
#  示例 2:
#
#  输入: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# 输出: 42
#  Related Topics 树 深度优先搜索
#  👍 601 👎 0
import pytest

from common_utils import TreeNode


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        """
        TODO
        Hard
        """
        max_sum = -0x80000000

        def getPathSumChildRec(node):
            nonlocal max_sum
            if not node:
                return 0
            # // max sum on the left and right sub-trees of node
            left_gain = max(0, getPathSumChildRec(node.left))
            right_gain = max(0, getPathSumChildRec(node.right))
            # // the price to start a new path where `node` is a highest node
            price_new = node.val + left_gain + right_gain
            # // update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_new)
            # //    // return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        getPathSumChildRec(root)
        return max_sum


@pytest.mark.parametrize("args,expected", [
    (TreeNode.initTreeSimple([1, None, 2, 3], [(2, 3)], [(0, 2)]), 6),
    pytest.param(TreeNode.initTreeSimple([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]), 47),
    pytest.param(TreeNode.initTreeSimple([1], [], []), 1),
])
def test_solutions(args, expected):
    assert Solution().maxPathSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
