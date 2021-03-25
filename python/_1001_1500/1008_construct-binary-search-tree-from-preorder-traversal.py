#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。 
# 
#  (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right
#  的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。） 
# 
#  
# 
#  示例： 
# 
#  输入：[8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= preorder.length <= 100 
#  先序 preorder 中的值是不同的。 
#  
#  Related Topics 树

"""
import math
from typing import List

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.idx = 0
        N = len(preorder)

        def helper(lower=-math.inf, upper=math.inf):
            if self.idx == N:
                return None
            val = preorder[self.idx]
            if val < lower or val > upper:
                return None
            self.idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        ans = helper()
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [8, 5, 1, 7, 10, 12],
            TreeNode(
                8,
                left=TreeNode(5, TreeNode(1), TreeNode(7)),
                right=TreeNode(10, right=TreeNode(12)),
            )
    ),
])
def test_solutions(args, expected):
    assert repr(Solution().bstFromPreorder(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
