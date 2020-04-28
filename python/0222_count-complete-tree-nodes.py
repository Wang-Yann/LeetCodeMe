#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:24:06
# @Last Modified : 2020-04-22 10:24:06
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        ans = []
        if not root:return 0
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return len(ans)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, left=TreeNode(2, TreeNode(4), TreeNode(5)),
                 right=TreeNode(3, left=TreeNode(6))
                 )

    ]
    lists = [x for x in samples]
    res = [sol.countNodes(x) for x in lists]
    print(res)
