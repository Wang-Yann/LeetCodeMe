#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:12:13
# @Last Modified : 2020-04-23 23:12:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        lookup = {v:i for i, v in enumerate(nums)}

        def helper(start, end):
            # print(start, end)
            if start > end:
                return None
            max_val = max(nums[start:end+1])
            max_index = lookup[max_val]
            root = TreeNode(max_val)
            root.left = helper(start, max_index - 1)
            root.right = helper(max_index + 1, end)
            return root

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [3, 2, 1, 6, 0, 5],
        []

    ]
    res = [sol.constructMaximumBinaryTree(args) for args in samples]
    print(res)
