#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。 
# 
#  只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。 
# 
#  编写一个判断两个二叉树是否是翻转等价的函数。这些树由根节点 root1 和 root2 给出。 
# 
#  
# 
#  示例： 
# 
#  输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,n
# ull,null,null,8,7]
# 输出：true
# 解释：我们翻转值为 1，3 以及 5 的三个节点。
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树最多有 100 个节点。 
#  每棵树中的每个值都是唯一的、在 [0, 99] 范围内的整数。 
#  
# 
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
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return helper(node1.left, node2.right) and helper(node1.right, node2.left) \
                   or helper(node1.left, node2.left) and helper(node1.right, node2.right)

        return helper(root1, root2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root1=TreeNode(
            1,
            left=TreeNode(2, left=TreeNode(4), right=TreeNode(5, TreeNode(7), TreeNode(8))),
            right=TreeNode(3, left=TreeNode(6))
        ),
        root2=TreeNode(
            1,
            left=TreeNode(3, right=TreeNode(6)),
            right=TreeNode(2, left=TreeNode(4), right=TreeNode(5, TreeNode(8), TreeNode(7)))
        )
    ), True],
])
def test_solutions(kw, expected):
    assert Solution().flipEquiv(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
