#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 17:14:28
# @Last Modified : 2020-08-04 17:14:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。 
# 
#  子树是树中的任意节点和它的所有后代构成的集合。 
# 
#  树的平均值是树中节点值的总和除以节点数。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：[5,6,1]
# 输出：6.00000
# 解释： 
# 以 value = 5 的节点作为子树的根节点，得到的平均值为 (5 + 6 + 1) / 3 = 4。
# 以 value = 6 的节点作为子树的根节点，得到的平均值为 6 / 1 = 6。
# 以 value = 1 的节点作为子树的根节点，得到的平均值为 1 / 1 = 1。
# 所以答案取最大值 6。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数介于 1 到 5000之间。 
#  每个节点的值介于 0 到 100000 之间。 
#  如果结果与标准答案的误差不超过 10^-5，那么该结果将被视为正确答案。 
#  
#  Related Topics 树 
#  👍 15 👎 0

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
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        """AC"""
        self.ans = -1

        def dfs(node):
            if not node:
                return 0, 0
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)
            ret_sum, ret_cnt = left_sum + right_sum + node.val, left_cnt + right_cnt + 1
            self.ans = max(self.ans, ret_sum / ret_cnt)
            return ret_sum, ret_cnt

        if not root:
            return 0
        dfs(root)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(5, left=TreeNode(6), right=TreeNode(1))
    ), 6.00000],
    [dict(
        root=TreeNode(120, left=TreeNode(30), right=TreeNode(30))
    ), 60.00000],
])
def test_solutions(kw, expected):
    assert Solution().maximumAverageSubtree(**kw) == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
