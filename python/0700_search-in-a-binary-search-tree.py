#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:26:17
# @Last Modified : 2020-04-24 16:26:17
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
#
#  例如，
#
#
# 给定二叉搜索树:
#
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# 和值: 2
#
#
#  你应该返回如下子树:
#
#
#       2
#      / \
#     1   3
#
#
#  在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
#  Related Topics 树
#  👍 71 👎 0
import pytest

from common_utils import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(4,
                        TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(7)
                        ),
          val=2), 2],
])
def test_solutions(kw, expected):
    res = Solution().searchBST(**kw)
    assert res == expected == None or res.val == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
