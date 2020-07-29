#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 19:36:50
# @Last Modified : 2020-07-29 19:36:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二叉树，你需要找出二叉树中最长的连续序列路径的长度。 
# 
#  请注意，该路径可以是递增的或者是递减。例如，[1,2,3,4] 和 [4,3,2,1] 都被认为是合法的，而路径 [1,2,4,3] 则不合法。另一方面，
# 路径可以是 子-父-子 顺序，并不一定是 父-子 顺序。 
# 
#  示例 1: 
# 
#  输入:
#         1
#        / \
#       2   3
# 输出: 2
# 解释: 最长的连续路径是 [1, 2] 或者 [2, 1]。
#  
# 
#  
# 
#  示例 2: 
# 
#  输入:
#         2
#        / \
#       1   3
# 输出: 3
# 解释: 最长的连续路径是 [1, 2, 3] 或者 [3, 2, 1]。
#  
# 
#  
# 
#  注意: 树上所有节点的值都在 [-1e7, 1e7] 范围内。 
#  Related Topics 树 
#  👍 29 👎 0

"""

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
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        树形DP
        GOOD
        """
        self.length = 0

        def helper(node):
            if node is None:
                return 0, 0
            left_inc, left_dec = helper(node.left)
            right_inc, right_dec = helper(node.right)

            cur_inc = cur_dec = 1
            if node.left:
                if node.val + 1 == node.left.val:
                    cur_inc = max(cur_inc, left_inc + 1)
                elif node.val - 1 == node.left.val:
                    cur_dec = max(cur_dec, left_dec + 1)
            if node.right:
                if node.val + 1 == node.right.val:
                    cur_inc = max(cur_inc, right_inc + 1)
                elif node.val - 1 == node.right.val:
                    cur_dec = max(cur_dec, right_dec + 1)

            self.length = max(self.length, cur_inc + cur_dec - 1)
            return cur_inc, cur_dec

        helper(root)
        return self.length


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1, TreeNode(2), TreeNode(3))), 2],
    [dict(root=TreeNode(2, TreeNode(1), TreeNode(3))), 3],
])
def test_solutions(kw, expected):
    assert Solution().longestConsecutive(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
