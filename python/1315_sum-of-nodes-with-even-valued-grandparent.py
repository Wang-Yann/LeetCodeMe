#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和： 
# 
#  
#  该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。） 
#  
# 
#  如果不存在祖父节点值为偶数的节点，那么返回 0 。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在 1 到 10^4 之间。 
#  每个节点的值在 1 到 100 之间。 
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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helper(node, p, gp):
            if not node:
                return 0
            val = 0
            if node and gp is not None and gp % 2 == 0:
                val = node.val
            return helper(node.left, node.val, p) + helper(node.right, node.val, p) + val

        return helper(root, None, None)


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            6,
            left=TreeNode(7, left=TreeNode(2, left=TreeNode(9)), right=TreeNode(7, TreeNode(1), TreeNode(4))),
            right=TreeNode(8, left=TreeNode(1), right=TreeNode(3, right=TreeNode(5))),
        )
    ), 18],
])
def test_solutions(kw, expected):
    assert Solution().sumEvenGrandparent(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
