#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 15:51:41
# @Last Modified : 2020-07-27 15:51:41
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0


# 给定一个二叉树，返回其结点 垂直方向（从上到下，逐列）遍历的值。
# 
#  如果两个结点在同一行和列，那么顺序则为 从左到右。 
# 
#  示例 1： 
# 
#  输入: [3,9,20,null,null,15,7]
# 
#    3
#   /\
#  /  \
# 9   20
#     /\
#    /  \
#   15   7 
# 
# 输出:
# 
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
#  
# 
#  示例 2: 
# 
#  输入: [3,9,8,4,0,1,7]
# 
#      3
#     /\
#    /  \
#   9    8
#   /\   /\
#  /  \ /  \
# 4   0 1   7 
# 
# 输出:
# 
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
#  
# 
#  示例 3: 
# 
#  输入: [3,9,8,4,0,1,7,null,null,null,2,5]（注意：0 的右侧子节点为 2，1 的左侧子节点为 5）
# 
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# 
# 输出:
# 
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 37 👎 0


import collections
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
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        """GOOD
        对于一棵树，我们设其根节点的位置为0。 对于任一非叶子节点，若其位置为x，设其左儿子的位置为x-1，右儿子位置为x+1
        """
        res = collections.defaultdict(list)
        dq = collections.deque()
        dq.append((root, 0))
        while dq:
            node, x = dq.popleft()
            if node:
                res[x].append(node.val)
                dq.append((node.left, x - 1))
                dq.append((node.right, x + 1))
        # print(res)
        return [res[i] for i in sorted(res)]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            3,
            left=TreeNode(9),
            right=TreeNode(20, TreeNode(15), TreeNode(7))
        )

    ),

        [
            [9],
            [3, 15],
            [20],
            [7]
        ]
    ],
    [dict(
        root=TreeNode(
            3,
            left=TreeNode(9, TreeNode(4), TreeNode(0)),
            right=TreeNode(8, TreeNode(1), TreeNode(7))
        )

    ),

        [
            [4],
            [9],
            [3, 0, 1],
            [8],
            [7]
        ]
    ],

    [dict(
        root=TreeNode(
            3,
            left=TreeNode(9, TreeNode(4), TreeNode(0, right=TreeNode(2))),
            right=TreeNode(8, TreeNode(1, left=TreeNode(5)), TreeNode(7))
        )

    ),

        [
          [4],
          [9,5],
          [3,0,1],
          [8,2],
          [7]
        ]
    ],
])
def test_solutions(kw, expected):
    assert Solution().verticalOrder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
