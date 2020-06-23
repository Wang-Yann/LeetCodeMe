#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下： 
# 
#  
#  选择二叉树中 任意 节点和一个方向（左或者右）。 
#  如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。 
#  改变前进方向：左变右或者右变左。 
#  重复第二步和第三步，直到你在树中无法继续移动。 
#  
# 
#  交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。 
# 
#  请你返回给定树中最长 交错路径 的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# 输出：3
# 解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,1,1,null,1,null,null,1,1,null,1]
# 输出：4
# 解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。
#  
# 
#  示例 3： 
# 
#  输入：root = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树最多有 50000 个节点。 
#  每个节点的值在 [1, 100] 之间。 
#  
#  Related Topics 树 动态规划

"""
import collections
import itertools

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

    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return -1, -1
            left, right = dfs(node.left), dfs(node.right)
            self.ans = max(left[1] + 1, right[0] + 1, self.ans)
            return left[1] + 1, right[0] + 1

        dfs(root)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def longestZigZag(self, root: TreeNode) -> int:
        """
        BFS
        记 f(u) 为从根到节点 u 的路径上以 u 结尾并且 u 是它父亲的左儿子的最长交错路径，
        g(u) 为从根到节点 u 的路径上以 u 结尾并且 u 是它父亲的右儿子的最长交错路径
        用二元组 (node, parent) 作为状态
        """
        f, g = collections.defaultdict(int), collections.defaultdict(int)
        q = collections.deque([(root, None)])
        while len(q) > 0:
            node, parent = q.popleft()
            if parent:
                if parent.left == node:
                    f[node] = g[parent] + 1
                else:
                    g[node] = f[parent] + 1
            if node.left:
                q.append((node.left, node))
            if node.right:
                q.append((node.right, node))

        return max(itertools.chain(f.values(), g.values(), [0]))


@pytest.mark.parametrize("args,expected", [
    (
            TreeNode(1, right=TreeNode(1, left=TreeNode(1),
                                       right=TreeNode(1, left=TreeNode(1, right=TreeNode(1, right=TreeNode(1))), right=TreeNode(1))))
            , 3),
    pytest.param(
        TreeNode(1, left=TreeNode(1,
                                  right=TreeNode(1, left=TreeNode(1, right=TreeNode(1)),
                                                 right=TreeNode(1))
                                  ),
                 right=TreeNode(1))
        , 4),
    (TreeNode(1), 0)
])
def test_solutions(args, expected):
    assert Solution().longestZigZag(args) == expected
    assert Solution1().longestZigZag(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
