#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 14:13:19
# @Last Modified : 2020-04-21 14:13:19
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """左闭右闭"""
        length = len(nums)
        if not length: return None

        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, length - 1)

    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        """左闭右开"""
        length = len(nums)
        if not length: return None

        def helper(l, r):
            if l == r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = helper(l, mid)
            root.right = helper(mid + 1, r)
            return root

        return helper(0, length)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [-10, -3, 0, 5, 9]
    ]
    res = [sol.sortedArrayToBST(x) for x in samples]
    print(res)
