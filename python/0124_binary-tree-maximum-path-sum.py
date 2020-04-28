#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 16:50:09
# @Last Modified : 2020-04-21 16:50:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        TODO
        Hard
        """
        max_sum = float("-inf")

        def getPathSumChildRec(node):
            nonlocal max_sum
            if not node: return 0
            # // max sum on the left and right sub-trees of node
            left_gain = max(0, getPathSumChildRec(node.left))
            right_gain = max(0, getPathSumChildRec(node.right))
            # // the price to start a new path where `node` is a highest node
            price_new = node.val + left_gain + right_gain
            # // update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_new)
            # //    // return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        getPathSumChildRec(root)
        return max_sum


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]),
        ([1], [], [])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.maxPathSum(x) for x in lists]
    print(res)
