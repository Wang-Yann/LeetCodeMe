#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。 
# 
#  由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6]
# 输出：110
# 解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,null,2,3,4,null,null,5,6]
# 输出：90
# 解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）
#  
# 
#  示例 3： 
# 
#  输入：root = [2,3,9,10,7,8,6,5,4,11,1]
# 输出：1025
#  
# 
#  示例 4： 
# 
#  输入：root = [1,1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树最多有 50000 个节点，且至少有 2 个节点。 
#  每个节点的值在 [1, 10000] 之间。 
#  
#  Related Topics 树 动态规划

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
    """后序遍历"""

    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10 ** 9 + 7
        sums = []

        def postOrderTraversal(node):
            if not node:
                return 0
            res = postOrderTraversal(node.left) + postOrderTraversal(node.right) + node.val
            sums.append(res)
            return res

        postOrderTraversal(root)
        # print(sums)
        ans = -0x80000000
        total = sums[-1]
        for i in range(len(sums) - 1):
            ans = max(ans, sums[i] * (total - sums[i]))
        return ans % MOD

# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    [TreeNode(1, left=TreeNode(2, TreeNode(4), TreeNode(5)), right=TreeNode(3, TreeNode(6))), 110],
    [TreeNode(1, right=TreeNode(2, left=TreeNode(3), right=TreeNode(4, TreeNode(5), TreeNode(6)))), 90],
    [TreeNode(2,
              left=TreeNode(3,
                            left=TreeNode(10, TreeNode(5), TreeNode(4)),
                            right=TreeNode(7, TreeNode(11), TreeNode(1))
                            ),
              right=TreeNode(9, TreeNode(8), TreeNode(6))

              ), 1025],
    [TreeNode(1, left=TreeNode(1)), 1],
])
def test_solutions(args, expected):
    assert Solution().maxProduct(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
