#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 21:44:39
# @Last Modified : 2020-04-22 21:44:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        queue = [root]
        ans = 0
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.pop(0)
                if i==0:
                    ans = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(1, left=TreeNode(2, right=TreeNode(4)),
                 right=TreeNode(3, TreeNode(5, TreeNode(7), TreeNode(6))))
    ]
    res = [sol.findBottomLeftValue(x) for x in samples]
    print(res)
