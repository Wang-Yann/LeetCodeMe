#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你 root1 和 root2 这两棵二叉搜索树。 
# 
#  请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。. 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
#  
# 
#  示例 2： 
# 
#  输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
# 输出：[-10,0,0,1,2,5,7,10]
#  
# 
#  示例 3： 
# 
#  输入：root1 = [], root2 = [5,1,7,0,2]
# 输出：[0,1,2,5,7]
#  
# 
#  示例 4： 
# 
#  输入：root1 = [0,-10,10], root2 = []
# 输出：[-10,0,10]
#  
# 
#  示例 5： 
# 
#  
# 
#  输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  每棵树最多有 5000 个节点。 
#  每个节点的值在 [-10^5, 10^5] 之间。 
#  
#  Related Topics 排序 树

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode, ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """Generator 很慢??"""
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        ans = []
        inorder(root1)
        inorder(root2)
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root1=TreeNode(2, TreeNode(1), TreeNode(4)),
        root2=TreeNode(1, TreeNode(0), TreeNode(3)),
    ), [0, 1, 1, 2, 3, 4]
    ],
    [dict(
        root1=TreeNode(0, TreeNode(-10), TreeNode(10)),
        root2=TreeNode(5, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(7)),
    ), [-10, 0, 0, 1, 2, 5, 7, 10]
    ],
    [dict(
        root1=None,
        root2=TreeNode(5, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(7)),
    ), [0, 1, 2, 5, 7]
    ],
    [dict(
        root1=TreeNode(0, TreeNode(-10), TreeNode(10)),
        root2=None,
    ), [-10, 0, 10]
    ],
])
def test_solutions(kw, expected):
    assert Solution().getAllElements(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
