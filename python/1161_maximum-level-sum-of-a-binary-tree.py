#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。 
# 
#  请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：[1,7,0,7,-8,null,null]
# 输出：2
# 解释：
# 第 1 层各元素之和为 1，
# 第 2 层各元素之和为 7 + 0 = 7，
# 第 3 层各元素之和为 7 + -8 = -1，
# 所以我们返回第 2 层的层号，它的层内元素之和最大。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数介于 1 和 10^4 之间 
#  -10^5 <= node.val <= 10^5 
#  
#  Related Topics 图

"""

import collections

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
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = []
        dq = collections.deque([root])
        while dq:
            row_sum = 0
            l = len(dq)
            for _ in range(l):
                node = dq.popleft()
                row_sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            levels.append(row_sum)
        return levels.index(max(levels))+1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(1, left=TreeNode(7, TreeNode(7), TreeNode(-8)), right=TreeNode(0)), 2)
])
def test_solutions(args, expected):
    assert Solution().maxLevelSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
