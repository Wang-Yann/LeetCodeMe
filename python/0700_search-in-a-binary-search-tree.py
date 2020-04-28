#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:26:17
# @Last Modified : 2020-04-24 16:26:17
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 2]

    ]
    lists = [x for x in samples]
    res = [sol.searchBST(*x) for x in lists]
    print(res)
