#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。 
# 
#  二叉搜索树的定义如下： 
# 
#  
#  任意节点的左子树中的键值都 小于 此节点的键值。 
#  任意节点的右子树中的键值都 大于 此节点的键值。 
#  任意节点的左子树和右子树都是二叉搜索树。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [4,3,null,1,2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。
#  
# 
#  示例 3： 
# 
#  输入：root = [-4,-2,-5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。
#  
# 
#  示例 4： 
# 
#  输入：root = [2,1,3]
# 输出：6
#  
# 
#  示例 5： 
# 
#  输入：root = [5,4,8,3,null,6,3]
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树最多有 40000 个节点。 
#  每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。 
#  
#  Related Topics 二叉搜索树 动态规划

"""

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxSumBST(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node: TreeNode):
            if not node:
                return True, 0, 0x7fffffff, -0x80000000
            l_is_bst, l_sum, l_min, l_max = dfs(node.left)
            r_is_bst, r_sum, r_min, r_max = dfs(node.right)
            if l_is_bst and r_is_bst and l_max < node.val < r_min:
                total = l_sum + r_sum + node.val
                self.ans = max(self.ans, total)
                return True, total, min(l_min, node.val), max(r_max, node.val)
            return False, 0, 0, 0

        dfs(root)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            TreeNode(1,
                     left=TreeNode(4, TreeNode(2, TreeNode(4))),
                     right=TreeNode(3, left=TreeNode(2), right=TreeNode(5, TreeNode(4), TreeNode(6))))
            , 20),
    pytest.param(TreeNode(4, left=TreeNode(3, TreeNode(1), TreeNode(2))), 2),
    pytest.param(TreeNode(-4, TreeNode(-2), TreeNode(-5)), 0),
    pytest.param(TreeNode(2, TreeNode(1), TreeNode(3)), 6),
    (TreeNode(5, left=TreeNode(4, left=TreeNode(3)), right=TreeNode(8, TreeNode(6), TreeNode(3))), 7)
])
def test_solutions(args, expected):
    assert Solution().maxSumBST(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
