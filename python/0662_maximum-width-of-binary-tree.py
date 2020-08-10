#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 11:47:35
# @Last Modified : 2020-04-24 11:47:35
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节
# 点为空。
#
#  每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
#
#  示例 1:
#
#
# 输入:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
#
#
#  示例 2:
#
#
# 输入:
#
#           1
#          /
#         3
#        / \
#       5   3
#
# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
#
#
#  示例 3:
#
#
# 输入:
#
#           1
#          / \
#         3   2
#        /
#       5
#
# 输出: 2
# 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
#
#
#  示例 4:
#
#
# 输入:
#
#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# 输出: 8
# 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
#
#
#  注意: 答案在32位有符号整数的表示范围内。
#  Related Topics 树
#  👍 115 👎 0

import pytest

from common_utils import TreeNode


class Solution0:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        TODO
        """
        leftmosts = {}

        def dfs(node, pos, depth):
            """深度优先搜索"""
            if not node: return 0
            if depth >= len(leftmosts):
                # 对于每一个深度,第一个到达的位置会被记录
                leftmosts[depth] = pos
            return max(
                pos - leftmosts[depth] + 1,
                dfs(node.left, pos * 2, depth + 1),
                dfs(node.right, pos * 2 + 1, depth + 1),
            )

        res = dfs(root, 1, 0)
        return res


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        leftmosts = {}
        self.ans = 0

        def dfs(node, pos=0, depth=0):
            """深度优先搜索"""
            if node:
                # 对于每一个深度,第一个到达的位置会被记录 ,
                # 重点,pos只会写一次.　等价
                # leftmosts.setdefault(depth, pos)
                if depth not in leftmosts:
                    leftmosts[depth] = pos
                self.ans = max(self.ans, pos - leftmosts[depth] + 1)
                dfs(node.left, pos * 2, depth + 1)
                dfs(node.right, pos * 2 + 1, depth + 1)

        dfs(root)
        return self.ans


@pytest.mark.parametrize("args,expected", [
    [TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, right=TreeNode(9))), 4],
    [TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3))), 2]
])
def test_solutions(args, expected):
    assert Solution().widthOfBinaryTree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
