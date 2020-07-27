#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 14:29:05
# @Last Modified : 2020-07-27 14:29:05
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。 
# 
#  该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。 
# 
#  这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。 
# 
#  示例 1： 
# 
#  输入:
# 
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# 
# 输出: 3
# 
# 解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3 
# 
#  示例 2： 
# 
#  输入:
# 
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# 
# 输出: 2 
# 
# 解析: 当中，最长连续序列是 2-3。注意，不是 3-2-1，所以返回 2。 
#  Related Topics 树 
#  👍 23 👎 0

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
        self.ans = 1

        def dfs(node, parent, cur_length):
            if not node:
                return
            if parent and node.val == parent.val + 1:
                cur_length += 1
            else:
                cur_length = 1
            self.ans = max(self.ans, cur_length)
            dfs(node.left, node, cur_length)
            dfs(node.right, node, cur_length)

        if not root:
            return 0
        dfs(root, None, 1)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1, right=TreeNode(3, left=TreeNode(2), right=TreeNode(4, right=TreeNode(5))))), 3],
    [dict(root=TreeNode(2, right=TreeNode(3, left=TreeNode(2, left=TreeNode(1))))), 2],
])
def test_solutions(kw, expected):
    assert Solution().longestConsecutive(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
