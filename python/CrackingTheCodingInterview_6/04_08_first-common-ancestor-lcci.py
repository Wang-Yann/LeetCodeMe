#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:27:15
# @Last Modified : 2020-07-12 21:27:15
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。 
# 
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#      3
#    / \
#   5   1
#  / \ / \
# 6  2 0  8
#   / \
#  7   4
#  
# 
#  示例 1: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。 
# 
#  示例 2: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。 
# 
#  说明: 
# 
#  所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。 
#  Related Topics 树 
#  👍 15 👎 0


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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in (p,q,None):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    q = TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, left=p, right=q)
    res = Solution().lowestCommonAncestor(root, p, q)
    assert repr(res) == repr(root)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
