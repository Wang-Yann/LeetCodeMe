#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。 
# 
#  提醒一下，二叉搜索树满足下列约束条件： 
# 
#  
#  节点的左子树仅包含键 小于 节点键的节点。 
#  节点的右子树仅包含键 大于 节点键的节点。 
#  左右子树也必须是二叉搜索树。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数介于 1 和 100 之间。 
#  每个节点的值介于 0 和 100 之间。 
#  给定的树为二叉搜索树。 
#  
# 
#  
# 
#  注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/ 相同
#  
#  Related Topics 二叉搜索树

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

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum_val = 0

        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.sum_val += node.val
            node.val = self.sum_val
            dfs(node.left)

        dfs(root)
        return root


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            TreeNode(4,
                     left=TreeNode(1, left=TreeNode(0), right=TreeNode(2, right=TreeNode(3))),
                     right=TreeNode(6, left=TreeNode(5), right=TreeNode(7, right=TreeNode(8)))
                     )
            , TreeNode(30,
                       left=TreeNode(36, left=TreeNode(36), right=TreeNode(35, right=TreeNode(33))),
                       right=TreeNode(21, left=TreeNode(26), right=TreeNode(15, right=TreeNode(8)))
                       )),
])
def test_solutions(args, expected):
    assert repr(Solution().bstToGst(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
