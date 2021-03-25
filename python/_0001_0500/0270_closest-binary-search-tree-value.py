#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 19:05:10
# @Last Modified : 2020-07-22 19:05:10
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。
# 
#  注意： 
# 
#  
#  给定的目标值 target 是一个浮点数 
#  题目保证在该二叉搜索树中只会存在一个最接近目标值的数 
#  
# 
#  示例： 
# 
#  输入: root = [4,2,5,1,3]，目标值 target = 3.714286
# 
#     4
#    / \
#   2   5
#  / \
# 1   3
# 
# 输出: 4
#  
#  Related Topics 树 二分查找 
#  👍 31 👎 0


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
    def closestValue(self, root: TreeNode, target: float) -> int:
        gap = closest = float("inf")
        while root:
            if abs(root.val - target) < gap:
                gap = abs(root.val - target)
                closest = root.val
            if target == root.val:
                break
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        return closest


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(4, left=TreeNode(2, TreeNode(1), TreeNode(3)), right=TreeNode(5)),
        target=3.714286

    ), 4],
])
def test_solutions(kw, expected):
    assert Solution().closestValue(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
