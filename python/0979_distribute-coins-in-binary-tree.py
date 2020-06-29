#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。 
# 
#  在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。 
# 
#  返回使每个结点上只有一枚硬币所需的移动次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[3,0,0]
# 输出：2
# 解释：从树的根结点开始，我们将一枚硬币移到它的左子结点上，一枚硬币移到它的右子结点上。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[0,3,0]
# 输出：3
# 解释：从根结点的左子结点开始，我们将两枚硬币移到根结点上 [移动两次]。然后，我们把一枚硬币从根结点移到右子结点上。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：[1,0,2]
# 输出：2
#  
# 
#  示例 4： 
# 
#  
# 
#  输入：[1,0,0,null,3]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1<= N <= 100 
#  0 <= node.val <= N 
#  
#  Related Topics 树 深度优先搜索

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
    def distributeCoins(self, root: TreeNode) -> int:
        """
        如果树的叶子仅包含 0 枚金币（与它所需相比，它的 过载量 为 -1），那么我们需要从它的父亲节点移动一枚金币到这个叶子节点上。如果说，一个叶子节点包含 4 枚金币（它的 过载量 为 3），那么我们需要将这个叶子节点中的 3 枚金币移动到别的地方去。总的来说，对于一个叶子节点，需要移动到它中或需要从它移动到它的父亲中的金币数量为 过载量 = Math.abs(num_coins - 1)。然后，在接下来的计算中，我们就再也不需要考虑这些已经考虑过的叶子节点了
     定义 dfs(node) 为这个节点所在的子树中金币的 过载量

        """
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(3, TreeNode(0), TreeNode(0)), 2),
    (TreeNode(0, TreeNode(3), TreeNode(0)), 3),
    (TreeNode(1, TreeNode(0), TreeNode(2)), 2),
    (TreeNode(1, TreeNode(0, right=TreeNode(3)), TreeNode(0)), 4),
])
def test_solutions(args, expected):
    assert Solution().distributeCoins(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
