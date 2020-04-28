#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 15:24:44
# @Last Modified : 2020-04-22 15:24:44
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        TODO Good
        """

        def getRobRecu(node):
            """return vals tuple ( with node,val without node)"""
            if not node:
                return 0, 0
            left, right = getRobRecu(node.left), getRobRecu(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)

        return max(getRobRecu(root))


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(3,
                 left=TreeNode(2, right=TreeNode(3)),
                 right=TreeNode(3, right=TreeNode(1))
                 ),
        TreeNode.initPreOrder([
            3, 4, 1, None, None, 3, None, None,
            5, None, 1, None, None
        ])

    ]
    lists = [x for x in samples]
    print(lists)
    res = [sol.rob(x) for x in lists]
    print(res)
