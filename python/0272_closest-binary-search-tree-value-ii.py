#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 22:18:47
# @Last Modified : 2020-07-22 22:18:47
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。 
# 
#  注意： 
# 
#  
#  给定的目标值 target 是一个浮点数 
#  你可以默认 k 值永远是有效的，即 k ≤ 总结点数 
#  题目保证该二叉搜索树中只会存在一种 k 个值集合最接近目标值 
#  
# 
#  示例： 
# 
#  输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2
# 
#     4
#    / \
#   2   5
#  / \
# 1   3
# 
# 输出: [4,3] 
# 
#  拓展： 
# 假设该二叉搜索树是平衡的，请问您是否能在小于 O(n)（n 为总结点数）的时间复杂度内解决该问题呢？ 
#  Related Topics 栈 树 
#  👍 36 👎 0

"""

from typing import List

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

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
        因为是BST，所以左边结点小于右边结点，中序遍历后是一个有序的数组，
        ，遍历过程中判断是否已经在res并且比较第0个值与target
        """
        if not root:
            return []
        res = []
        self.inorder(root, target, k, res)
        return res

    def inorder(self, root, target, k, res):
        if not root:
            return
        self.inorder(root.left, target, k, res)
        if k > len(res):
            res.append(root.val)
        elif abs(res[0] - target) > abs(root.val - target):
            res.pop(0)
            res.append(root.val)
        self.inorder(root.right, target, k, res)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(root=TreeNode(
        4,
        left=TreeNode(2, TreeNode(1), TreeNode(3)),
        right=TreeNode(5)
    ), target=3.714286, k=2), [4, 3]],

])
def test_solutions(kwargs, expected):
    assert sorted(Solution().closestKValues(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
