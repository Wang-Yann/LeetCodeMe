#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树
#  👍 312 👎 0

from typing import List

import pytest

from common_utils import TreeNode


class Solution0:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(node, result):
            if node is None:
                return
            result.append(node.val)
            helper(node.left, result)
            helper(node.right, result)

        helper(root, res)
        return res


class Solution:
    """迭代　基"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)

        return ans


@pytest.mark.parametrize("args,expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [3, 9, 20, 15, 7])
])
def test_solutions(args, expected):
    assert Solution().preorderTraversal(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
