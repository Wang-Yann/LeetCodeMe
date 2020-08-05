#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 16:43:40
# @Last Modified : 2020-08-05 16:43:40
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出两棵二叉搜索树，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。 
# 
#  如果可以找到返回 True，否则返回 False。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root1 = [2,1,4], root2 = [1,0,3], target = 5
# 输出：true
# 解释：2 加 3 和为 5 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  每棵树上最多有 5000 个节点。 
#  -10^9 <= target, node.val <= 10^9 
#  
#  Related Topics 二叉搜索树 
#  👍 16 👎 0

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
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        """AC"""

        @functools.lru_cache(None)
        def helper(node1, node2):
            if not node1 or not node2:
                return False
            sum_val = node1.val + node2.val
            if sum_val == target:
                return True
            elif sum_val < target:
                return helper(node1.right, node2) or helper(node1, node2.right)
            else:
                return helper(node1.left, node2) or helper(node1, node2.left)

        return helper(root1, root2)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(
        root1=TreeNode(2, TreeNode(1), TreeNode(4)),
        root2=TreeNode(1, TreeNode(0), TreeNode(3)),
        target=5
    ), True],
    [dict(
        root1=TreeNode(0, TreeNode(-10), TreeNode(10)),
        root2=TreeNode(5, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(7)),
        target=18
    ), False],
])
def test_solutions(kw, expected):
    assert Solution().twoSumBSTs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
