#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:49:42
# @Last Modified : 2020-04-22 10:49:42
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root or not k:return None
        cur = root
        stack = []
        idx=0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            idx+=1
            if idx==k:
                return cur.val
            cur=cur.right


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(3,
                 left=TreeNode(1, right=TreeNode(2)),
                 right=TreeNode(4)
                 ),
        TreeNode(5,
                 left=TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                 right=TreeNode(6)
                 )

    ]
    lists = [x for x in samples]
    res = [sol.kthSmallest(x,3) for x in lists]
    print(res)
