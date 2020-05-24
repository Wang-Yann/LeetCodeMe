#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#  
# 
#  示例 2: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 
#  
# 
#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉树中。 
#  
# 
#  注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a
# -binary-tree/ 
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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    sol = Solution()
    p = TreeNode(5,
                 left=TreeNode(6),
                 right=TreeNode(2, TreeNode(7), TreeNode(4))
                 )
    q = TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, left=p, right=q)

    resA = sol.lowestCommonAncestor(root, p, q)
    assert repr(resA) == repr(root)


def test_solutions1():
    sol = Solution()
    pA = TreeNode(4)
    qA = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), pA))
    rootA = TreeNode(3, left=qA, right=TreeNode(1, TreeNode(0), TreeNode(8)))

    resA = sol.lowestCommonAncestor(rootA, pA, qA)
    assert repr(resA) == repr(qA)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
