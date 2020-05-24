#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0


"""
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5] 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
#  
# 
#  示例 2: 
# 
#  输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。 
# 
#  
# 
#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉搜索树中。 
#  
# 
#  注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a
# -binary-search-tree/ 
#  Related Topics 树

"""
from common_utils import TreeNode
import pytest
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p # 保证 p.val < q.val
        while root:
            if root.val < p.val: # p,q 都在 root 的右子树中
                root = root.right # 遍历至右子节点
            elif root.val > q.val: # p,q 都在 root 的左子树中
                root = root.left # 遍历至左子节点
            else: break
        return root


def test_solutions():
    sol = Solution()
    p1A = TreeNode(2,
                   left=TreeNode(0),
                   right=TreeNode(4, TreeNode(3), TreeNode(5))
                   )
    p2A = TreeNode(8, TreeNode(7), TreeNode(9))
    rootA = TreeNode(6, left=p1A, right=p2A)

    resA = sol.lowestCommonAncestor(rootA, p1A, p2A)
    assert repr(resA) == repr(rootA)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
