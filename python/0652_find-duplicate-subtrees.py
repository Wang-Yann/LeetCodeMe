#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 18:12:49
# @Last Modified : 2020-04-22 18:12:49
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections
from typing import List

from common_utils import TreeNode


class Solution:
    """ O(N2)"""

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        results = []
        lookup = collections.defaultdict(int)

        def post_order_traversal(node):
            """Use PostOrder show String as key"""
            if not node: return ""
            key_str = "({}|{}|{})".format(
                post_order_traversal(node.left),
                node.val,
                post_order_traversal(node.right),
            )
            if lookup[key_str] == 1:
                results.append(node)
            lookup[key_str] += 1
            return key_str

        post_order_traversal(root)
        return results


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1,
                 left=TreeNode(2, right=TreeNode(4)),
                 right=TreeNode(3, left=TreeNode(2, TreeNode(4)),
                                right=TreeNode(4))

                 ),
        TreeNode(1, TreeNode(1), TreeNode(1)),
        TreeNode(0,
                 left=TreeNode(0, TreeNode(0)),
                 right=TreeNode(0, right=TreeNode(0, right=TreeNode(0)))
                 )
    ]
    lists = [x for x in samples]
    res = [sol.findDuplicateSubtrees(x) for x in lists]
    print(res)
