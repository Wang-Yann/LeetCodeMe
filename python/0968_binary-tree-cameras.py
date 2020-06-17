#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二叉树，我们在树的节点上安装摄像头。 
# 
#  节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。 
# 
#  计算监控树的所有节点所需的最小摄像头数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[0,0,null,0,0]
# 输出：1
# 解释：如图所示，一台摄像头足以监控所有节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：[0,0,null,0,null,0,null,null,0]
# 输出：2
# 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
#  
# 
#  
# 提示： 
# 
#  
#  给定树的节点数的范围是 [1, 1000]。 
#  每个节点的值都是 0。 
#  
#  Related Topics 树 深度优先搜索 动态规划

"""

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
    def minCameraCover(self, root: TreeNode) -> int:
        """后序遍历"""
        COVERED, UNCOVERED, CAMERA = range(3)
        ans = 0

        def dfs(node):
            nonlocal ans
            left = dfs(node.left) if node.left else COVERED
            right = dfs(node.right) if node.right else COVERED
            if left == UNCOVERED or right == UNCOVERED:
                ans += 1
                return CAMERA
            if left == CAMERA or right == CAMERA:
                return COVERED
            return UNCOVERED

        if dfs(root) == UNCOVERED:
            ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    """官方
    难写出
    """

    def minCameraCover(self, root):
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node:
                return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])


@pytest.mark.parametrize("args,expected", [
    (TreeNode(0, left=TreeNode(0, TreeNode(0), TreeNode(0))), 1),
    (TreeNode(0, left=TreeNode(0, left=TreeNode(0, left=TreeNode(0, right=TreeNode(0))))), 2),
])
def test_solutions(args, expected):
    assert Solution().minCameraCover(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
