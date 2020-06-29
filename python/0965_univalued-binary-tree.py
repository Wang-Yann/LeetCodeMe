#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。 
# 
#  只有给定的树是单值二叉树时，才返回 true；否则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[1,1,1,1,1,null,1]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[2,2,2,5,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定树的节点数范围是 [1, 100]。 
#  每个节点的值都是整数，范围为 [0, 99] 。 
#  
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
    def isUnivalTree(self, root: TreeNode) -> bool:

        def helper(node):
            if not node:
                return True
            if node.val != val:
                return False
            return helper(node.left) and helper(node.right)

        if not root:
            return True
        val = root.val
        return helper(root)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(1, left=TreeNode(1, TreeNode(1), TreeNode(1)), right=TreeNode(1, right=TreeNode(1))), True),
    (TreeNode(2, left=TreeNode(2, TreeNode(2), TreeNode(5)), right=TreeNode(2)), False),
])
def test_solutions(args, expected):
    assert Solution().isUnivalTree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
