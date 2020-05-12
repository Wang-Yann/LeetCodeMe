#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一棵二叉搜索树，请找出其中第k大的节点。 
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4 
# 
#  示例 2: 
# 
#  输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4 
# 
#  
# 
#  限制： 
# 
#  1 ≤ k ≤ 二叉搜索树元素个数 
#  Related Topics 树

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

    def kthLargest(self, root: TreeNode, k: int) -> int:
        def helper(node):
            nonlocal k
            nonlocal res
            if not node:
                return None
            helper(node.right)
            if k==0:
                return
            k-=1
            if k==0:
                res = node.val
            helper(node.left)
        res =0
        helper(root)
        return res




# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(root=TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4)), k=1), 4),
])
def test_solutions(kwargs, expected):
    assert Solution().kthLargest(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
