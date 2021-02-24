#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 10:18:14
# @Last Modified : 2021-02-24 10:18:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ： 
# 
#  
#  二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。 
#  偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增 
#  奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减 
#  
# 
#  给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# 输出：true
# 解释：每一层的节点值分别是：
# 0 层：[1]
# 1 层：[10,4]
# 2 层：[3,7,9]
# 3 层：[12,8,6,2]
# 由于 0 层和 2 层上的节点值都是奇数且严格递增，而 1 层和 3 层上的节点值都是偶数且严格递减，因此这是一棵奇偶树。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [5,4,2,3,3,7]
# 输出：false
# 解释：每一层的节点值分别是：
# 0 层：[5]
# 1 层：[4,2]
# 2 层：[3,3,7]
# 2 层上的节点值不满足严格递增的条件，所以这不是一棵奇偶树。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [5,9,1,3,5,7]
# 输出：false
# 解释：1 层上的节点值应为偶数。
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1]
# 输出：true
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数在范围 [1, 105] 内 
#  1 <= Node.val <= 106 
#  
#  Related Topics 树 
#  👍 8 👎 0

"""

import collections

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
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        is_even = True
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if is_even:
                    if node.val % 2 == 0: return False
                    if prev and prev.val >= node.val: return False
                else:
                    if node.val % 2 == 1: return False
                    if prev and prev.val <= node.val: return False
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                prev = node
            is_even = not is_even
        return True

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        1,
        left=TreeNode(10, left=TreeNode(3, TreeNode(12), TreeNode(8))),
        right=TreeNode(4, left=TreeNode(7, left=TreeNode(6)), right=TreeNode(9, right=TreeNode(2)))
    )), True],

    [dict(root=TreeNode(
        5,
        left=TreeNode(4, TreeNode(3), TreeNode(3)),
        right=TreeNode(2, left=TreeNode(7))
    )), False],

    [dict(root=TreeNode(
        5,
        left=TreeNode(9, TreeNode(3), TreeNode(3)),
        right=TreeNode(1, left=TreeNode(7))
    )), False],
    [dict(root=TreeNode(1, )), True],
    [dict(root=TreeNode(
        11,
        left=TreeNode(8,
                      left=TreeNode(1, TreeNode(30, TreeNode(7)), TreeNode(20)),
                      right=TreeNode(3, TreeNode(18), TreeNode(16)), ),
        right=TreeNode(6,
                       left=TreeNode(9, TreeNode(12), TreeNode(10)),
                       right=TreeNode(11, TreeNode(4), TreeNode(2)), ),
    )), True
    ]

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().isEvenOddTree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
