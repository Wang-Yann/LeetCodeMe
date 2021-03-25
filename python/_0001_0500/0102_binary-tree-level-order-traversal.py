#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层次遍历结果：
#
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 565 👎 0

from collections import deque
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = []
        Q = []
        cur_level = 0
        Q.append((cur_level, root))
        tmp = []
        while Q:
            level, node = Q.pop(0)
            if not node:
                continue
            if level == cur_level:
                tmp.append(node.val)
            else:
                ans.append(tmp)
                tmp = [node.val]
                cur_level = level
            if node.left:
                Q.append((cur_level + 1, node.left))
            if node.right:
                Q.append((cur_level + 1, node.right))
        if tmp:
            ans.append(tmp)
        return ans


class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        def helper(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return res


class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root: return levels
        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return levels


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)))
    ),
        [
            [3],
            [9, 20],
            [15, 7]
        ]
    ],
])
@pytest.mark.parametrize("CLS", [
    Solution, Solution1, Solution2
])
def test_solutions(kw, expected, CLS):
    assert CLS().levelOrder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
