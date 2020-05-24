#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 11:03:16
# @Last Modified : 2020-04-22 11:03:16
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import pytest

from common_utils import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if not p: return q
        if not q: return p
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
