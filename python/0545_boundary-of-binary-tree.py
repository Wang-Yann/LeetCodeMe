#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 18:14:52
# @Last Modified : 2020-07-29 18:14:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给定一棵二叉树，以逆时针顺序从根开始返回其边界。边界按顺序包括左边界、叶子结点和右边界而不包括重复的结点。 (结点的值可能重复)
# 
#  左边界的定义是从根到最左侧结点的路径。右边界的定义是从根到最右侧结点的路径。若根没有左子树或右子树，则根自身就是左边界或右边界。注意该定义只对输入的二叉树
# 有效，而对子树无效。 
# 
#  最左侧结点的定义是：在左子树存在时总是优先访问，如果不存在左子树则访问右子树。重复以上操作，首先抵达的结点就是最左侧结点。 
# 
#  最右侧结点的定义方式相同，只是将左替换成右。 
# 
#  示例 1 
# 
#  输入:
#   1
#    \
#     2
#    / \
#   3   4
# 
# 输出:
# [1, 3, 4, 2]
# 
# 解析:
# 根不存在左子树，故根自身即为左边界。
# 叶子结点是3和4。
# 右边界是1，2，4。注意逆时针顺序输出需要你输出时调整右边界顺序。
# 以逆时针顺序无重复地排列边界，得到答案[1,3,4,2]。
#  
# 
#  
# 
#  示例 2 
# 
#  输入:
#     ____1_____
#    /          \
#   2            3
#  / \          / 
# 4   5        6   
#    / \      / \
#   7   8    9  10  
#        
# 输出:
# [1,2,4,7,8,9,10,6,3]
# 
# 解析:
# 左边界是结点1,2,4。(根据定义，4是最左侧结点)
# 叶子结点是结点4,7,8,9,10。
# 右边界是结点1,3,6,10。(10是最右侧结点)
# 以逆时针顺序无重复地排列边界，得到答案 [1,2,4,7,8,9,10,6,3]。
#  
# 
#  
#  Related Topics 树 
#  👍 25 👎 0


from typing import List

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
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if not root.left and not root.right:
            return [root.val]

        left_boundary = self.find_left_boundary(root.left)
        leaves = self.find_leaves(root)
        right_boundary = self.find_right_boundary(root.right)

        if left_boundary and leaves and left_boundary[-1] == leaves[0]:
            leaves = leaves[1:]
        if leaves and right_boundary and leaves[-1] == right_boundary[-1]:
            leaves = leaves[:-1]
        return [root.val] + left_boundary + leaves + list(reversed(right_boundary))

    def leaves(self, root, nodes):
        """同下方"""

        if not root:
            return
        if not root.left and not root.right:
            nodes.append(root.val)
            return
        self.leaves(root.left, nodes)
        self.leaves(root.right, nodes)

    def find_leaves(self, root):
        stack = [root]
        leaves = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaves

    def find_left_boundary(self, root):
        left_boundary = []
        while root is not None:
            left_boundary.append(root.val)
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                break
        return left_boundary

    def find_right_boundary(self, root):
        right_boundary = []
        while root is not None:
            right_boundary.append(root.val)
            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            else:
                break
        return right_boundary


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        1,
        right=TreeNode(2, TreeNode(3), TreeNode(4)))), [1, 3, 4, 2]],
    [dict(root=TreeNode(
        1,
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(5, TreeNode(7), TreeNode(8))),
        right=TreeNode(3, left=TreeNode(6, TreeNode(9), TreeNode(10)))
    )), [1, 2, 4, 7, 8, 9, 10, 6, 3]],
    [dict(root=TreeNode(1)), [1]],
])
def test_solutions(kw, expected):
    assert Solution().boundaryOfBinaryTree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
