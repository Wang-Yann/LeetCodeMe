#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 14:13:19
# @Last Modified : 2020-04-21 14:13:19
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
#  示例:
#
#  给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  Related Topics 树 深度优先搜索
#  👍 517 👎 0
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """左闭右闭"""
        length = len(nums)
        if not length: return None

        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, length - 1)

    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        """左闭右开"""
        length = len(nums)
        if not length: return None

        def helper(l, r):
            if l == r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, length)


@pytest.mark.parametrize("args,expected", [
    ([-10, -3, 0, 5, 9],
     [
         TreeNode(0, left=TreeNode(-3, left=TreeNode(-10)), right=TreeNode(9, left=TreeNode(5))),
         TreeNode(0, left=TreeNode(-10, right=TreeNode(-3)), right=TreeNode(5, right=TreeNode(9))),
     ])
])
def test_solutions(args, expected):
    res1 = Solution().sortedArrayToBST(args)
    res2 = Solution().sortedArrayToBST1(args)
    assert repr(res1) in [repr(x) for x in expected]
    assert repr(res2) in [repr(x) for x in expected]


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
