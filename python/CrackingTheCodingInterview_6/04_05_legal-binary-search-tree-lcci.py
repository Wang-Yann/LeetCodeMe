#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:18:15
# @Last Modified : 2020-07-12 21:18:15
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 实现一个函数，检查一棵二叉树是否为二叉搜索树。示例 1: 输入:     2    / \   1   3 输出: true 示例 2: 输入:     5
#     / \   1   4      / \     3   6 输出: false 解释: 输入为: [5,1,4,null,null,3,6]。    
#   根节点的值为 5 ，但是其右子节点值为 4 。 Related Topics 树 深度优先搜索 
#  👍 20 👎 0


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

    def isValidBST(self, root: TreeNode) -> bool:
        nodes = []

        def dfs(node):
            if node:
                dfs(node.left)
                nodes.append(node.val)
                dfs(node.right)

        dfs(root)
        return nodes == sorted(set(nodes))


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kwargs,expected", [
    [dict(root=TreeNode(2, TreeNode(1), TreeNode(3))), True],
    [dict(root=TreeNode(1, TreeNode(1), TreeNode(1))), False],

])
def test_solutions(kwargs, expected):
    assert Solution().isValidBST(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
