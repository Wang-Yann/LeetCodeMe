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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        A little hard
        双递归
        """

        def getPathSum(cur, sum_val):
            if not cur:
                return 0
            cur_val = sum_val + cur.val
            cur_cnt = int(cur_val == sum)
            return cur_cnt + getPathSum(cur.left, cur_val) + getPathSum(cur.right, cur_val)

        if not root: return 0
        return getPathSum(root, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([10, 5, -3, 3, 2, 11, 3, -2, 1],
         [(0, 1), (1, 3), (3, 6)],
         [(0, 2), (2, 5), (1, 4), (4, 8), (3, 7)]
         ),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]),
        ([1], [], [])

    ]
    sums = [8,
            12, 1
            ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.pathSum(x, y) for x, y in itertools.zip_longest(lists, sums)]
    print(res)
