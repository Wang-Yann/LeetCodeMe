#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 16:50:09
# @Last Modified : 2020-04-21 16:50:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import itertools

from common_utils import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if root.val == sum and not root.left and not root.right:
            return True
        res_left, res_right = False, False
        if root.left:
            res_left = self.hasPathSum(root.left, sum - root.val)
        if root.right:
            res_right =  self.hasPathSum(root.right, sum - root.val)
        return res_left or res_right


    def hasPathSumSS(self, root: TreeNode, sum: int) -> bool:
        """
        sum - root.val
        
        
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right,
                                                                             sum - root.val)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]),
        ([1], [], [])

    ]
    sums = [7, 12, 1]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.hasPathSum(x, y) for x, y in itertools.zip_longest(lists, sums)]
    print(res)
