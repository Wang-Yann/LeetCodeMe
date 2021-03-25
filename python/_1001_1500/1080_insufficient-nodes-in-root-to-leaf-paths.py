#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一棵二叉树的根 root，请你考虑它所有 从根到叶的路径：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点） 
# 
#  假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为「不足节点」，需要被删除。 
# 
#  请你删除所有不足节点，并返回生成的二叉树的根。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
# 
# 输出：[1,2,3,4,null,null,7,8,9,null,14]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
# 
# 输出：[5,4,8,11,null,17,4,7,null,null,null,5] 
# 
#  示例 3： 
# 
#  
# 输入：root = [5,-6,-6], limit = 0
# 输出：[] 
# 
#  
# 
#  提示： 
# 
#  
#  给定的树有 1 到 5000 个节点 
#  -10^5 <= node.val <= 10^5 
#  -10^9 <= limit <= 10^9 
#  
# 
#  
#  Related Topics 深度优先搜索

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
    """
    Intuition
        If root is leaf,
        we compare the limit and root.val,
        and return the result directly.

        If root is not leaf,
        we recursively call the function on root's children with limit = limit - root.val.

        Note that if a node become a new leaf,
        it means it has no valid path leading to an original leaf,
        we need to remove it.
    """
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        if root.left == root.right:
            return None if root.val < limit else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            1,
            left=TreeNode(2,
                          left=TreeNode(4, TreeNode(8), TreeNode(9)),
                          right=TreeNode(-99, TreeNode(-99), TreeNode(-99))
                          ),
            right=TreeNode(3,
                           left=TreeNode(-99, TreeNode(12), TreeNode(13)),
                           right=TreeNode(7, TreeNode(-99), TreeNode(14)),
                           )
        ), limit=1
    ), TreeNode(1,
                left=TreeNode(2,
                              left=TreeNode(4, TreeNode(8), TreeNode(9)),
                              ),
                right=TreeNode(3, right=TreeNode(7, right=TreeNode(14))
                               )

                )
    ],
    [dict(
        root=TreeNode(
            5,
            left=TreeNode(4,
                          left=TreeNode(11, TreeNode(7), TreeNode(1)),
                          ),
            right=TreeNode(8,
                           left=TreeNode(17),
                           right=TreeNode(4, TreeNode(5), TreeNode(3)),
                           )
        ), limit=22
    ), TreeNode(
        5,
        left=TreeNode(4,
                      left=TreeNode(11, TreeNode(7)),
                      ),
        right=TreeNode(8,
                       left=TreeNode(17),
                       right=TreeNode(4, TreeNode(5)),
                       )
    )],
    [dict(
        root=TreeNode(5, left=TreeNode(-6), right=TreeNode(-6)), limit=0
    ), None],
])
def test_solutions(kw, expected):
    assert repr(Solution().sufficientSubset(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
