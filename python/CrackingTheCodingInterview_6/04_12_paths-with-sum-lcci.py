#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:39:19
# @Last Modified : 2020-07-12 21:39:19
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的
# 根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。 
# 
#  示例: 
# 给定如下二叉树，以及目标和 sum = 22， 
# 
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  3
# 解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7] 
# 
#  提示： 
# 
#  
#  节点总数 <= 10000 
#  
#  Related Topics 树 深度优先搜索 
#  👍 23 👎 0


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
    """TODO"""

    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, sum_val):
            if not node:
                return 0
            res = 1 if node.val == sum_val else 0
            return res + dfs(node.left, sum_val - node.val) + dfs(node.right, sum_val - node.val)

        if not root:
            return 0
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        root=TreeNode(
            5,
            left=TreeNode(4, left=TreeNode(11, TreeNode(7), TreeNode(2))),
            right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, TreeNode(5), TreeNode(1))),
        ), sum=22

    ), 3],

])
def test_solutions(kwargs, expected):
    assert Solution().pathSum(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
