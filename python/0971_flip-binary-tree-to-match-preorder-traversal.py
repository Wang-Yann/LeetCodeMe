#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个有 N 个节点的二叉树，每个节点都有一个不同于其他节点且处于 {1, ..., N} 中的值。 
# 
#  通过交换节点的左子节点和右子节点，可以翻转该二叉树中的节点。 
# 
#  考虑从根节点开始的先序遍历报告的 N 值序列。将这一 N 值序列称为树的行程。 
# 
#  （回想一下，节点的先序遍历意味着我们报告当前节点的值，然后先序遍历左子节点，再先序遍历右子节点。） 
# 
#  我们的目标是翻转最少的树中节点，以便树的行程与给定的行程 voyage 相匹配。 
# 
#  如果可以，则返回翻转的所有节点的值的列表。你可以按任何顺序返回答案。 
# 
#  如果不能，则返回列表 [-1]。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [1,2], voyage = [2,1]
# 输出：[-1]
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,2,3], voyage = [1,3,2]
# 输出：[1]
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：root = [1,2,3], voyage = [1,2,3]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 100 
#  
#  Related Topics 树 深度优先搜索

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
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.idx = 0
        self.flipped = []

        def dfs(node):
            if not node:
                return
            if node.val != voyage[self.idx]:
                self.flipped = [-1]
                return
            self.idx += 1
            if self.idx < N and node.left and node.left.val != voyage[self.idx]:
                self.flipped.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        N = len(voyage)
        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1, left=TreeNode(2)), voyage=[2, 1]), [-1]],
    [dict(root=TreeNode(1, TreeNode(2), TreeNode(3)), voyage=[1, 3, 2]), [1]],
    [dict(root=TreeNode(1, TreeNode(2), TreeNode(3)), voyage=[1, 2, 3]), []],
])
def test_solutions(kw, expected):
    assert sorted(Solution().flipMatchVoyage(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
