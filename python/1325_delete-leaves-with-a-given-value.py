#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 23:34:35
# @Last Modified : 2020-07-06 23:34:35
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。 
# 
#  注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。 
# 
#  也就是说，你需要重复此过程直到不能继续删除。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [1,2,3,2,null,2,4], target = 2
# 输出：[1,null,3,null,4]
# 解释：
# 上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。
# 有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,3,3,3,2], target = 3
# 输出：[1,3,null,null,2]
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：root = [1,2,null,2,null,2], target = 2
# 输出：[1]
# 解释：每一步都删除一个绿色的叶子节点（值为 2）。 
# 
#  示例 4： 
# 
#  输入：root = [1,1,1], target = 1
# 输出：[]
#  
# 
#  示例 5： 
# 
#  输入：root = [1,2,3], target = 1
# 输出：[1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target <= 1000 
#  每一棵树最多有 3000 个节点。 
#  每一个节点值的范围是 [1, 1000] 。 
#  
#  Related Topics 树 
#  👍 22 👎 0

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

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        root=TreeNode(1, left=TreeNode(2, left=TreeNode(2)), right=TreeNode(3, TreeNode(2), TreeNode(4))), target=2
    ),
     TreeNode(1, right=TreeNode(3, right=TreeNode(4)))),

    pytest.param(dict(
        root=TreeNode(1, left=TreeNode(3, TreeNode(3), TreeNode(2)), right=TreeNode(3)), target=3),
        TreeNode(1, left=TreeNode(3, right=TreeNode(2)))
    ),
    (dict(
        root=TreeNode(1, left=TreeNode(2, left=TreeNode(2, left=TreeNode(2)))), target=2
    ),
     TreeNode(1)),
    (dict(
        root=TreeNode(1, left=TreeNode(1), right=TreeNode(1)), target=1
    ),
     None
    ),

])
def test_solutions(kwargs, expected):
    res = Solution().removeLeafNodes(**kwargs)
    assert repr(res) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
