#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 11:03:16
# @Last Modified : 2020-04-22 11:03:16
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

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
#  Related Topics 树
#  👍 335 👎 0
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if not p:
            return q
        if not q:
            return p
        cur = root
        p_val, q_val = (p.val, q.val) if p.val < q.val else (q.val, p.val)
        while cur:
            if p_val <= cur.val <= q_val:
                return cur
            elif cur.val > q_val:
                cur = cur.left
            elif cur.val < p_val:
                cur = cur.right
        return cur


class Solution1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getPath(root: TreeNode, target: TreeNode) -> List[TreeNode]:
            path = list()
            node = root
            while node != target:
                path.append(node)
                if target.val < node.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path

        path_p = getPath(root, p)
        path_q = getPath(root, q)
        ancestor = None
        for u, v in zip(path_p, path_q):
            if u == v:
                ancestor = u
            else:
                break

        return ancestor


@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(SolutionCLS):
    sol = SolutionCLS()
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
