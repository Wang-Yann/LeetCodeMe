#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 17:03:04
# @Last Modified : 2020-07-27 17:03:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，其中最大指的是子树节点数最多的。 
# 
#  注意: 
# 子树必须包含其所有后代。 
# 
#  示例: 
# 
#  输入: [10,5,15,1,8,null,7]
# 
#    10 
#    / \ 
#   5  15 
#  / \   \ 
# 1   8   7
# 
# 输出: 3
# 解释: 高亮部分为最大的 BST 子树。
#      返回值 3 在这个样例中为子树大小。
#  
# 
#  进阶: 
# 你能想出用 O(n) 的时间复杂度解决这个问题吗？ 
#  Related Topics 树 
#  👍 44 👎 0

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
    def largestBSTSubtree(self, root: TreeNode) -> int:
        """
        GOOD
        为空节点时，返回float("inf"), float("-inf")，这样它的任何父节点都将合法
        如果当前节点不满足约束条件，返回float("-inf"), float("inf")，这样它的任何父节点都将不合法
        """
        def helper(node):
            if not node:
                return float('inf'), float('-inf'), 0
            l_min, l_max, l_size = helper(node.left)
            r_min, r_max, r_size = helper(node.right)
            if l_max < node.val < r_min:
                return min(l_min, node.val), max(node.val, r_max), 1 + l_size + r_size
            return float('-inf'), float('inf'), max(l_size, r_size)

        return helper(root)[2]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        10,
        left=TreeNode(5, TreeNode(1), TreeNode(8)),
        right=TreeNode(15, right=TreeNode(7))

    )), 3],
])
def test_solutions(kw, expected):
    assert Solution().largestBSTSubtree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
