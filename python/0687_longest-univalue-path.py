#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:01:50
# @Last Modified : 2020-04-24 16:01:50
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
#  注意：两个节点之间的路径长度由它们之间的边数表示。
#
#  示例 1:
#
#  输入:
#
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
#
#
#  输出:
#
#
# 2
#
#
#  示例 2:
#
#  输入:
#
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
#
#
#  输出:
#
#
# 2
#
#
#  注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
#  Related Topics 树 递归
#  👍 304 👎 0

from common_utils import TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        TODO
            我们可以将任何路径（具有相同值的节点）看作是最多两个从其根延伸出的箭头。
            具体地说，路径的根将是唯一节点，因此该节点的父节点不会出现在该路径中,
            而箭头将是根在该路径中只有一个子节点的路径。
            当我们计算箭头长度时，候选答案将是该节点在两个方向上的箭头之和.
        """
        self.ans = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0
            self.ans = max(self.ans, left + right)
            return max(left, right)

        dfs(root)
        return self.ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)),
                 TreeNode(5, TreeNode(6), right=TreeNode(5)))

    ]
    lists = [x for x in samples]
    res = [sol.longestUnivaluePath(x) for x in lists]
    print(res)
