#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 11:22:51
# @Last Modified : 2020-07-10 11:22:51
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。 
# 
#  请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [2,3,1,3,1,null,1]
# 输出：2 
# 解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
#      在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排
# 列 [1,2,1] 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [2,1,1,1,3,null,null,null,null,null,1]
# 输出：1 
# 解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
#      这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。
#  
# 
#  示例 3： 
# 
#  输入：root = [9]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定二叉树的节点数目在 1 到 10^5 之间。 
#  节点值在 1 到 9 之间。 
#  
#  Related Topics 位运算 树 深度优先搜索 
#  👍 11 👎 0

"""

import collections

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    """
    根据 n & (n - 1) 来消除1 所以判断是否为回文数字的条件就变成了
    (n == 0 || (n & (n - 1)) == 0)
    """

    def pseudoPalindromicPaths(self, root):
        def dfs(node, count):
            if not node:
                return 0
            count ^= (1 << node.val)
            return int(
                node.left == node.right
                and count & (count - 1) == 0
            ) + dfs(node.left, count) + dfs(node.right, count)

        return dfs(root, 0)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """AC"""

        def check(vals):
            counter = collections.Counter(vals)
            return sum(v % 2 for v in counter.values()) in (1, 0)

        self.ans = 0

        def dfs(node, path):
            if not node:
                return
            if node.left is None and node.right is None:
                if check(path):
                    self.ans += 1
            if node.left:
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])

        dfs(root, [root.val])
        return self.ans


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(2,
                      left=TreeNode(3, TreeNode(3), TreeNode(1)),
                      right=TreeNode(1, right=TreeNode(1))
                      )
    ), 2],
    [dict(
        root=TreeNode(2,
                      left=TreeNode(1, TreeNode(1), TreeNode(3, right=TreeNode(1))),
                      right=TreeNode(1)
                      )
    ), 1],
    [dict(
        root=TreeNode(9)
    ), 1],
])
def test_solutions(kw, expected):
    assert Solution().pseudoPalindromicPaths(**kw) == expected
    assert Solution1().pseudoPalindromicPaths(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
