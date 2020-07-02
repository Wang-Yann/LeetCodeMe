#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n
#  各不相同。 
# 
#  
# 
#  游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时， 
# 
#  「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）； 
# 
#  「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。 
# 
#  「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。 
# 
#  
# 
#  之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。 
# 
#  如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。 
# 
#  若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。 
# 
#  
# 
#  现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true；若无法获胜，就请返回 false。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# 输出：True
# 解释：第二个玩家可以选择值为 2 的节点。
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的根节点为 root，树上由 n 个节点，节点上的值从 1 到 n 各不相同。 
#  n 为奇数。 
#  1 <= x <= n <= 100 
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

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        """
        https://leetcode-cn.com/problems/binary-tree-coloring-game/solution/shen-du-you-xian-sou-suo-python3-by-smoon1989-3/
        如何确定蓝色是否有必胜策略，就可以转换为，被红色点切割的三个连通分量中，是否存在一个连通分量，大小大于所有结点数目的一半
        """
        self.red_left, self.red_right = 0, 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val == x:
                self.red_left = left
                self.red_right = right
            return left + right + 1

        dfs(root)
        parent = n - self.red_left - self.red_right - 1
        judge = [parent, self.red_left, self.red_right]
        return any(v > n // 2 for v in judge)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        root=TreeNode(
            1,
            left=TreeNode(2,
                          left=TreeNode(4, TreeNode(8), TreeNode(9)),
                          right=TreeNode(5, TreeNode(10), TreeNode(11))
                          ),
            right=TreeNode(3, TreeNode(6), TreeNode(7))

        ), n=11, x=3
    ), True),
])
def test_solutions(kwargs, expected):
    assert Solution().btreeGameWinningMove(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
