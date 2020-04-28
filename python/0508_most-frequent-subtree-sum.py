#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 22:54:28
# @Last Modified : 2020-04-22 22:54:28
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
from typing import List

from common_utils import TreeNode


class Solution:

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        lookup = collections.defaultdict(int)
        if not root:
            return []

        def postPreOrderTraversalSum(cur):
            if not cur:
                return 0
            sum_key = sum([postPreOrderTraversalSum(cur.left),
                           cur.val, postPreOrderTraversalSum(cur.right)])
            lookup[sum_key] += 1
            return sum_key

        postPreOrderTraversalSum(root)
        mv = max(lookup.values())

        return [k for k, v in lookup.items() if v == mv]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(5, TreeNode(2), TreeNode(-3)),
        TreeNode(5, TreeNode(2), TreeNode(-5)),
    ]
    res = [sol.findFrequentTreeSum(x) for x in samples]
    print(res)
