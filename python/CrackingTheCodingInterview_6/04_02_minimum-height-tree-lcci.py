#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:03:29
# @Last Modified : 2020-07-12 21:03:29
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。示例: 给定有序数组: [-10,-3,0,5,9], 一个可能
# 的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：           0          / \        -3 
#   9        /   /      -10  5 Related Topics 树 深度优先搜索 
#  👍 37 👎 0


"""

from typing import List

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(start, end):
            if start > end:
                return None
            mid = (start + end) >> 1
            root = TreeNode(nums[mid])
            root.left = helper(start, mid-1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(nums) - 1)

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [-10, -3, 0, 5, 9]
            , 3),
])
def test_solutions(args, expected):
    res = Solution().sortedArrayToBST(args)

    def getHeight(node):
        if not node:
            return 0
        return max(getHeight(node.left), getHeight(node.right)) + 1

    assert getHeight(res) == 3


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
