#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 16:50:09
# @Last Modified : 2020-04-21 16:50:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
#  找出路径和等于给定数值的路径总数。
#
#  路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
#  二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
#  示例：
#
#  root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
#
#  Related Topics 树
#  👍 491 👎 0

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
