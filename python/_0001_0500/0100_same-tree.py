#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#  示例 1:
#
#  输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
#
#  示例 2:
#
#  输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
#
#
#  示例 3:
#
#  输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# 输出: false
#
#  Related Topics 树 深度优先搜索
#  👍 398 👎 0

import pytest

from common_utils import TreeNode


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val \
               and self.isSameTree(p.left, q.left) \
               and self.isSameTree(p.right, q.right)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        p=TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
        q=TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    ), True],
    [dict(
        p=TreeNode(1, left=TreeNode(2)),
        q=TreeNode(1, right=TreeNode(2))
    ), False],
    [dict(
        p=TreeNode(1, left=TreeNode(2), right=TreeNode(1)),
        q=TreeNode(1, left=TreeNode(1), right=TreeNode(2))
    ), False],
])
def test_solutions(kw, expected):
    assert Solution().isSameTree(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
