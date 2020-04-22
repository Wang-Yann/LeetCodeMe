#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 22:09:57
# @Last Modified : 2020-04-22 22:09:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:

        def in_order_traversal(cur):
            if not cur:
                return []
            stack = []
            res = []
            cur =root
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            return res

        results = in_order_traversal(root)
        # print(results)
        if len(results) <= 1:
            return None
        else:
            delta = float("inf")
            for i in range(1, len(results)):
                delta = min(abs(results[i] - results[i - 1]),delta)
            return delta


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, right=TreeNode(3, TreeNode(2))),
        TreeNode(12),
        None
    ]
    res = [sol.getMinimumDifference(x) for x in samples]
    print(res)
