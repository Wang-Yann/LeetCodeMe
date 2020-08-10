#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 11:06:04
# @Last Modified : 2020-04-24 11:06:04
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：
#
#
#  行数 m 应当等于给定二叉树的高度。
#  列数 n 应当总是奇数。
#  根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分
# ，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，
# 如果两个子树都为空则不需要为它们留出任何空间。
#  每个未使用的空间应包含一个空的字符串""。
#  使用相同的规则输出子树。
#
#
#  示例 1:
#
#
# 输入:
#      1
#     /
#    2
# 输出:
# [["", "1", ""],
#  ["2", "", ""]]
#
#
#  示例 2:
#
#
# 输入:
#      1
#     / \
#    2   3
#     \
#      4
# 输出:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
#
#
#  示例 3:
#
#
# 输入:
#       1
#      / \
#     2   5
#    /
#   3
#  /
# 4
# 输出:
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
#
#
#  注意: 二叉树的高度在范围 [1, 10] 中。
#  Related Topics 树
#  👍 64 👎 0


from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getWidth(root):
            if not root:
                return 0
            return 2 * max(getWidth(root.left), getWidth(root.right)) + 1

        def getHeight(root):
            if not root:
                return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1

        def preorderTraversal(root, level, left, right):
            if not root:
                return
            mid = (left + right) >> 1
            result[level][mid] = str(root.val)
            preorderTraversal(root.left, level + 1, left, mid - 1)
            preorderTraversal(root.right, level + 1, mid + 1, right)

        h, w = getHeight(root), getWidth(root)
        result = [[""] * w for _ in range(h)]
        preorderTraversal(root, 0, 0, w - 1)
        return result


@pytest.mark.parametrize("args,expected", [
    [TreeNode(1, TreeNode(2)), [['', '1', ''], ['2', '', '']]],
    [TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3)),
     [['', '', '', '1', '', '', ''], ['', '2', '', '', '', '3', ''], ['', '', '4', '', '', '', '']]],
    [None, []],
])
def test_solutions(args, expected):
    assert Solution().printTree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
