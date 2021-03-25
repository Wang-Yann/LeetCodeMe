#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-07 23:54:04
# @Last Modified : 2020-07-07 23:54:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。 
# 
#  其中，克隆树 cloned 是原始树 original 的一个 副本 。 
# 
#  请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）
# 。 
# 
#  
# 
#  注意： 
# 
#  
#  你 不能 对两棵二叉树，以及 target 节点进行更改。 
#  只能 返回对克隆树 cloned 中已有的节点的引用。 
#  
# 
#  
#  
# 
#  进阶：如果树中允许出现值相同的节点，你将如何解答？ 
# 
#  
# 
#  
#  
# 
#  示例 1: 
# 
#  
# 
#  输入: tree = [7,4,3,null,null,6,19], target = 3
# 输出: 3
# 解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点
# （其他示例类似）。 
# 
#  示例 2: 
# 
#  
# 
#  输入: tree = [7], target =  7
# 输出: 7
#  
# 
#  示例 3: 
# 
#  
# 
#  输入: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
# 输出: 4
#  
# 
#  示例 4: 
# 
#  
# 
#  输入: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
# 输出: 5
#  
# 
#  示例 5: 
# 
#  
# 
#  输入: tree = [1,2,null,3], target = 2
# 输出: 2 
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量范围为 [1, 10^4] 。 
#  同一棵树中，没有值相同的节点。 
#  target 节点是树 original 中的一个节点，并且不会是 null 。 
#  
#  Related Topics 树 
#  👍 7 👎 0


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

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def in_order(node):
            if node:
                yield node
                yield from in_order(node.left)
                yield from in_order(node.right)

        for n1, n2 in zip(in_order(original), in_order(cloned)):
            if n1 == target:
                # For local test
                # if n1.val == target.val:
                return n2


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        original=TreeNode(7, left=TreeNode(4), right=TreeNode(3, TreeNode(6), TreeNode(9))),
        cloned=TreeNode(7, left=TreeNode(4), right=TreeNode(3, TreeNode(6), TreeNode(9))),
        target=TreeNode(3, TreeNode(6), TreeNode(9)),
    ), TreeNode(3, TreeNode(6), TreeNode(9))],
    [dict(
        original=TreeNode(7),
        cloned=TreeNode(7),
        target=TreeNode(7),
    ), TreeNode(7)],

])
def test_solutions(kwargs, expected):
    assert repr(Solution().getTargetCopy(**kwargs)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
