#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 18:12:49
# @Last Modified : 2020-04-22 18:12:49
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
#  两棵树重复是指它们具有相同的结构以及相同的结点值。
#
#  示例 1：
#
#          1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
#
#
#  下面是两个重复的子树：
#
#        2
#      /
#     4
#
#
#  和
#
#      4
#
#
#  因此，你需要以列表的形式返回上述重复子树的根结点。
#  Related Topics 树
#  👍 126 👎 0

import collections
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    """ O(N2)"""

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        results = []
        lookup = collections.defaultdict(int)

        def post_order_traversal(node):
            """Use PostOrder show String as key"""
            if not node:
                return ""
            key_str = "({}|{}|{})".format(
                post_order_traversal(node.left),
                node.val,
                post_order_traversal(node.right),
            )
            if lookup[key_str] == 1:
                results.append(node)
            lookup[key_str] += 1
            return key_str

        post_order_traversal(root)
        return results


@pytest.mark.parametrize("args,expected", [
    (TreeNode(1,
              left=TreeNode(2, right=TreeNode(4)),
              right=TreeNode(3, left=TreeNode(2, TreeNode(4)),
                             right=TreeNode(4))

              ), [['4']]),
    (TreeNode(1, TreeNode(1), TreeNode(1)),
     [['1']]
     ),
    (TreeNode(0,
              left=TreeNode(0, TreeNode(0)),
              right=TreeNode(0, right=TreeNode(0, right=TreeNode(0)))
              ),
     [['0']]
     )
])
def test_solutions(args, expected):
    res = Solution().findDuplicateSubtrees(args)
    assert repr(res) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
