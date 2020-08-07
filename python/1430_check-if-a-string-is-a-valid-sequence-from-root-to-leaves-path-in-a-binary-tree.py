#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 16:28:10
# @Last Modified : 2020-08-07 16:28:10
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二叉树，我们称从根节点到任意叶节点的任意路径中的节点值所构成的序列为该二叉树的一个 “有效序列” 。检查一个给定的序列是否是给定二叉树的一个 “有效
# 序列” 。 
# 
#  我们以整数数组 arr 的形式给出这个序列。从根节点到任意叶节点的任意路径中的节点值所构成的序列都是这个二叉树的 “有效序列” 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
# 输出：true
# 解释：
# 路径 0 -> 1 -> 0 -> 1 是一个“有效序列”（图中的绿色节点）。
# 其他的“有效序列”是：
# 0 -> 1 -> 1 -> 0 
# 0 -> 0 -> 0
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
# 输出：false 
# 解释：路径 0 -> 0 -> 1 不存在，所以这不是一个“序列”。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
# 输出：false
# 解释：路径 0 -> 1 -> 1 是一个序列，但不是一个“有效序列”（译者注：因为序列的终点不是叶节点）。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 5000 
#  0 <= arr[i] <= 9 
#  每个节点的值的取值范围是 [0 - 9] 
#  
#  Related Topics 树 
#  👍 0 👎 0

"""

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


class Solution(object):
    def isValidSequence(self, root, arr):
        N = len(arr)

        def dfs(node, depth):
            if not node or depth == N or node.val != arr[depth]:
                return False
            if depth + 1 == N and not node.left and not node.right:
                return True
            return dfs(node.left, depth + 1) or dfs(node.right, depth + 1)

        return dfs(root, 0)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def helper(node, path):
            # print(path)
            if not node:
                return False
            if node.left is None and node.right is None:
                return arr == path + [node.val]
            return helper(node.left, path + [node.val]) or helper(node.right, path + [node.val])

        return helper(root, [])


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            0,
            left=TreeNode(1,
                          left=TreeNode(0, right=TreeNode(1)),
                          right=TreeNode(1, TreeNode(0), TreeNode(0)),
                          ),
            right=TreeNode(0, left=TreeNode(0))
        )
        , arr=[0, 1, 0, 1]), True],
    [dict(
        root=TreeNode(
            0,
            left=TreeNode(1,
                          left=TreeNode(0, right=TreeNode(1)),
                          right=TreeNode(1, TreeNode(0), TreeNode(0)),
                          ),
            right=TreeNode(0, left=TreeNode(0))
        ),
        arr=[0, 0, 1]), False],
    [dict(root=TreeNode(
        0,
        left=TreeNode(1,
                      left=TreeNode(0, right=TreeNode(1)),
                      right=TreeNode(1, TreeNode(0), TreeNode(0)),
                      ),
        right=TreeNode(0, left=TreeNode(0))
    ), arr=[0, 1, 1]), False],
])
def test_solutions(kw, expected):
    assert Solution().isValidSequence(**kw) == expected
    assert Solution1().isValidSequence(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
