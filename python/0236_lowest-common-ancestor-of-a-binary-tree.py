#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 11:03:16
# @Last Modified : 2020-04-22 11:03:16
# @Mail          : rock@get.com.mm
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
#  Related Topics 树

"""
import pytest

from common_utils import TreeNode


class Solution:
    def lowestCommonAncestorMe(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """笨方法．提交运行会超限制 [原因是加了打印...]
        见方法下　
        """
        if not root: return None
        results = []
        p_val, q_val = p.val, q.val

        def dfs(path, node):
            if not node:
                return
            if node.val == p_val:
                results.append(path + [node])
            elif node.val == q_val:
                results.append(path + [node])
            if len(results) == 2:
                return
            if node.left:
                dfs(path + [node], node.left)
            if node.right:
                dfs(path + [node], node.right)

        dfs([], root)
        # print("Results",results,len(results))
        path_p, path_q = results
        i = 0
        lp, lq = len(path_p), len(path_q)
        ans = root
        while i <= lp - 1 and i <= lq - 1:
            if path_p[i].val != path_q[i].val:
                break
            ans = path_p[i]
            i += 1
        return ans

    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parents = {root: None}
        # Iterate until we find both the nodes p and q
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]
        return q


class Solution1:
    def lowestCommonAncestor(self, root, p, q):
        """Good """
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 1. If the current subtree contains both p and q,
        #    return their LCA.
        # 2. If only one of them is in that subtree,
        #    return that one of them.
        # 3. If neither of them is in that subtree,
        #    return the node of that subtree.
        return root if left and right else left or right


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

