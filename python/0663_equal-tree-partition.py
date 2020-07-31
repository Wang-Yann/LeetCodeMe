#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 10:36:18
# @Last Modified : 2020-07-31 10:36:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一棵有 n 个结点的二叉树，你的任务是检查是否可以通过去掉树上的一条边将树分成两棵，且这两棵树结点之和相等。 
# 
#  样例 1: 
# 
#  输入:     
#     5
#    / \
#   10 10
#     /  \
#    2   3
# 
# 输出: True
# 解释: 
#     5
#    / 
#   10
#       
# 和: 15
# 
#    10
#   /  \
#  2    3
# 
# 和: 15
#  
# 
#  
# 
#  样例 2: 
# 
#  输入:     
#     1
#    / \
#   2  10
#     /  \
#    2   20
# 
# 输出: False
# 解释: 无法通过移除一条树边将这棵树划分成结点之和相等的两棵子树。
#  
# 
#  
# 
#  注释 : 
# 
#  
#  树上结点的权值范围 [-100000, 100000]。 
#  1 <= n <= 10000 
#  
# 
#  
#  Related Topics 树 
#  👍 17 👎 0

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
    def checkEqualTree(self, root: TreeNode) -> bool:
        """AC"""
        lookup = collections.defaultdict(int)

        # @functools.lru_cache(None)
        def dfs(node):
            if node in lookup:
                return lookup[node]
            ans = node.val
            if node.left:
                ans += dfs(node.left)
            if node.right:
                ans += dfs(node.right)
            lookup[node] = ans
            return ans

        dfs(root)
        total = lookup.pop(root)
        if total % 2:
            return False
        target = total // 2
        # print(lookup)
        return target in lookup.values()


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(5, left=TreeNode(10), right=TreeNode(10, TreeNode(2), TreeNode(3))), True),
    (TreeNode(1, left=TreeNode(2), right=TreeNode(10, TreeNode(2), TreeNode(10))), False),
    (TreeNode(0), False),
    (TreeNode(0, TreeNode(0)), True),
    (TreeNode(0, TreeNode(-1), TreeNode(1)), False)
])
def test_solutions(args, expected):
    assert Solution().checkEqualTree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
