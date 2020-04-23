#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 15:00:18
# @Last Modified : 2020-04-23 15:00:18
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        Todo
        """

        def postOrder(cur, tilt):
            if not cur: return 0, tilt
            left_val, tilt = postOrder(cur.left, tilt)
            right_val, tilt = postOrder(cur.right, tilt)
            tilt += abs(left_val - right_val)
            return left_val + right_val + cur.val, tilt

        res = postOrder(root, 0)
        # print("Res", res)
        return res[1]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
        TreeNode(1, left=TreeNode(2, TreeNode(4)), right=TreeNode(3)),
        TreeNode(1),
        TreeNode(1, TreeNode(2, left=TreeNode(4)), TreeNode(3, left=TreeNode(5))),
        None
    ]
    lists = [x for x in samples]
    res = [sol.findTilt(x) for x in lists]
    print(res)
