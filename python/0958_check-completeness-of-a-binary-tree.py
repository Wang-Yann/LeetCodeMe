#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二叉树，确定它是否是一个完全二叉树。 
# 
#  百度百科中对完全二叉树的定义如下： 
# 
#  若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：
# 第 h 层可能包含 1~ 2h 个节点。） 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的结点没有尽可能靠向左侧。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中将会有 1 到 100 个结点。 
#  
#  Related Topics 树

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
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2 * v))
                nodes.append((node.right, 2 * v + 1))

        return nodes[-1][1] == len(nodes)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(1, left=TreeNode(2, TreeNode(4), TreeNode(5)), right=TreeNode(3, TreeNode(6))), True),
    (TreeNode(1, left=TreeNode(2, TreeNode(4), TreeNode(5)), right=TreeNode(3, right=TreeNode(7))), False),
])
def test_solutions(args, expected):
    assert Solution().isCompleteTree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
