#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一棵二叉树，请你返回层数最深的叶子节点的和。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在 1 到 10^4 之间。 
#  每个节点的值在 1 到 100 之间。 
#  
#  Related Topics 树 深度优先搜索

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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level = []
        dq = collections.deque([root])
        while dq:
            level.clear()
            length = len(dq)
            for _ in range(length):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return sum(level or [0])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            1,
            left=TreeNode(2, left=TreeNode(4, left=TreeNode(7)), right=TreeNode(5)),
            right=TreeNode(3, right=TreeNode(6, right=TreeNode(8)))
        )
    ), 15],
])
def test_solutions(kw, expected):
    assert Solution().deepestLeavesSum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
