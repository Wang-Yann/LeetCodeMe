#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 14:17:27
# @Last Modified : 2020-04-23 14:17:27
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节
# 点值之和。
#
#
#
#  例如：
#
#  输入: 原始二叉搜索树:
#               5
#             /   \
#            2     13
#
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13
#
#
#
#
#  注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-s
# um-tree/ 相同
#  Related Topics 树
#  👍 281 👎 0
import copy

import pytest

from common_utils import TreeNode


class Solution0:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def helper(node, cur_sum):
            if not node:
                return 0
            if node.right:
                cur_sum = helper(node.right, cur_sum)
            cur_sum += node.val
            node.val = cur_sum
            if node.left:
                cur_sum = helper(node.left, cur_sum)
            return cur_sum

        helper(root, 0)
        return root


class Solution1:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """从右向左的中序遍历"""
        cur = root
        stack = []
        total_sum = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            total_sum += cur.val
            cur.val = total_sum
            cur = cur.left
        return root


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """ 反序中序遍历该二叉搜索树"""
        self.accu = 0

        def dfs(node):
            if node:
                dfs(node.right)
                self.accu += node.val
                node.val = self.accu
                dfs(node.left)

        dfs(root)
        return root


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(5, TreeNode(2), TreeNode(13))),
     TreeNode(18, TreeNode(20), TreeNode(13))],
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution, Solution0, Solution1
])
def test_solutions(kw, expected, SolutionCLS):
    assert repr(SolutionCLS().convertBST(**copy.deepcopy(kw))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
