#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 14:44:33
# @Last Modified : 2020-04-24 14:44:33
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """中序遍历"""
        if not root: return None
        min_val, ans = root.val, float("inf")
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val != min_val:
                ans = min(ans, cur.val)
            cur = cur.right
        return ans if ans != float("inf") else -1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(2, TreeNode(2, TreeNode(5, TreeNode(5), TreeNode(7)))),
        TreeNode(2, TreeNode(2), TreeNode(2))

    ]
    lists = [x for x in samples]
    res = [sol.findSecondMinimumValue(x) for x in lists]
    print(res)
