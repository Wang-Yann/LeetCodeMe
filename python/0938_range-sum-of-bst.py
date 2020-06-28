#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。 
# 
#  二叉搜索树保证具有唯一的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
# 输出：32
#  
# 
#  示例 2： 
# 
#  输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的结点数量最多为 10000 个。 
#  最终的答案保证小于 2^31。 
#  
#  Related Topics 树 递归

"""
import functools

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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        @functools.lru_cache(None)
        def helper(node):
            if not node:
                return 0
            if node.val < L:
                return helper(node.right)
            elif node.val > R:
                return helper(node.left)
            else:
                return helper(node.left) + helper(node.right) + node.val

        return helper(root)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        10, left=TreeNode(5, TreeNode(3), TreeNode(7)),
        right=TreeNode(15, right=TreeNode(18))
    ), L=7, R=15), 32],
    [dict(root=TreeNode(
        10,
        left=TreeNode(5, TreeNode(3, left=TreeNode(1)), TreeNode(7, left=TreeNode(6))),
        right=TreeNode(15, TreeNode(13), TreeNode(18))
    ), L=6, R=10), 23],
])
def test_solutions(kw, expected):
    assert Solution().rangeSumBST(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
