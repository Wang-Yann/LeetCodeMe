#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 15:44:32
# @Last Modified : 2020-04-23 15:44:32
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isEqual(cur_s, cur_t):
            if not cur_s and not cur_t: return True
            if not (cur_s and cur_t): return False
            return cur_s.val==cur_t.val \
                   and isEqual(cur_s.left, cur_t.left) \
                   and isEqual(cur_s.right, cur_t.right)

        if not t: return True
        if not s: return False
        stack = [s]
        while stack:
            cur = stack.pop()
            if cur.val == t.val and isEqual(cur, t):
                return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False


if __name__ == '__main__':
    sol = Solution()
    samples = [
        (TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
         TreeNode(4, TreeNode(1), TreeNode(2))) ,
        (TreeNode(3, TreeNode(4, TreeNode(1,TreeNode(1)), TreeNode(2)), TreeNode(5)),
         TreeNode(4, TreeNode(1), TreeNode(2)))

    ]
    lists = [x for x in samples]
    res = [sol.isSubtree(*x) for x in lists]
    print(res)
