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
        """
        后序遍历
        贪心算法
        Return 0 if it's a leaf.
        Return 1 if it's a parent of a leaf, with a camera on this node.
        Return 2 if it's coverd, without a camera on this node.
        """
        UNCOVERED, CAMERA, COVERED = range(3)
        self.ans = 0
        dummy = TreeNode(-1)
        dummy.left = root

        def dfs(node):
            if not node:
                return COVERED
            left = dfs(node.left)
            right = dfs(node.right)
            if left == UNCOVERED or right == UNCOVERED:
                self.ans += 1
                return CAMERA
            elif left == CAMERA or right == CAMERA:
                return COVERED
            else:
                return UNCOVERED

        dfs(dummy)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    """官方
       难写出
    """

    def minCameraCover(self, root):
        """
        状态 a： root 必须放置摄像头的情况下，覆盖整棵树需要的摄像头数目。
        状态 b：覆盖整棵树需要的摄像头数目，无论  root 是否放置摄像头。
        状态 c：覆盖两棵子树需要的摄像头数目，无论节点  root 本身是否被监控到。
        根据它们的定义，一定有 a≥b≥c

        """

        def dfs(node):
            if not node:
                return float("inf"), 0, 0

            la, lb, lc = dfs(node.left)
            ra, rb, rc = dfs(node.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return a, b, c

        a, b, c = dfs(root)
        return b


@pytest.mark.parametrize("args,expected", [
    (TreeNode(0, left=TreeNode(0, TreeNode(0), TreeNode(0))), 1),
    (TreeNode(0, left=TreeNode(0, left=TreeNode(0, left=TreeNode(0, right=TreeNode(0))))), 2),
    (TreeNode(0), 1),
])
def test_solutions(args, expected):
    assert Solution().minCameraCover(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
