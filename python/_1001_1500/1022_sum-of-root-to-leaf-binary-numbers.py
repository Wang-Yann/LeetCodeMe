#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 ->
#  0 -> 1，那么它表示二进制数 01101，也就是 13 。 
# 
#  对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。 
# 
#  以 10^9 + 7 为模，返回这些数字之和。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：[1,0,1,0,1,0,1]
# 输出：22
# 解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的结点数介于 1 和 1000 之间。 
#  node.val 为 0 或 1 。 
#  
#  Related Topics 树

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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        MOD = 10 ** 9 + 7

        def dfs(node, path):
            if not node:
                return 0
            path += str(node.val)
            if node.left is None and node.right is None:
                return int(path, 2) % MOD
            return (dfs(node.left, path) + dfs(node.right, path)) % MOD

        ans = dfs(root, "")
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (TreeNode(1,
              left=TreeNode(0, TreeNode(0), TreeNode(1)),
              right=TreeNode(1, TreeNode(0), TreeNode(1)),
              ), 22)
])
def test_solutions(args, expected):
    assert Solution().sumRootToLeaf(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
