#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 16:48:35
# @Last Modified : 2020-04-23 16:48:35
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ""
        s = str(t.val)
        if t.left or t.right:
            s += "(" + self.tree2str(t.left) + ")"
        if t.right:
            s += "(" + self.tree2str(t.right) + ")"
        return s


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, left=TreeNode(2, TreeNode(4)), right=TreeNode(3)),
        TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))

    ]
    lists = [x for x in samples]
    res = [sol.tree2str(x) for x in lists]
    print(res)
