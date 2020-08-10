#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:12:13
# @Last Modified : 2020-04-23 23:12:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
#
#
#  二叉树的根是数组中的最大元素。
#  左子树是通过数组中最大值左边部分构造出的最大二叉树。
#  右子树是通过数组中最大值右边部分构造出的最大二叉树。
#
#
#  通过给定的数组构建最大二叉树，并且输出这个树的根节点。
#
#
#
#  示例 ：
#
#  输入：[3,2,1,6,0,5]
# 输出：返回下面这棵树的根节点：
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
#
#
#
#
#  提示：
#
#
#  给定的数组的大小在 [1, 1000] 之间。
#
#  Related Topics 树
#  👍 168 👎 0

from typing import List

import pytest

from common_utils import TreeNode


class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        lookup = {v: i for i, v in enumerate(nums)}

        def helper(start, end):
            # print(start, end)
            if start > end:
                return None
            max_val = max(nums[start:end + 1])
            max_index = lookup[max_val]
            root = TreeNode(max_val)
            root.left = helper(start, max_index - 1)
            root.right = helper(max_index + 1, end)
            return root

        return helper(0, len(nums) - 1)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[3, 2, 1, 6, 0, 5]), TreeNode(
        6,
        TreeNode(3, right=TreeNode(2, right=TreeNode(1))),
        TreeNode(5, left=TreeNode(0))
    )],
])
def test_solutions(kw, expected):
    assert repr(Solution().constructMaximumBinaryTree(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
