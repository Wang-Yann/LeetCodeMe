#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 15:24:44
# @Last Modified : 2020-04-22 15:24:44
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“
# 房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
#  计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
#  示例 1:
#
#  输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
#  示例 2:
#
#  输入: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#
#  Related Topics 树 深度优先搜索
#  👍 422 👎 0

import functools

import pytest

from common_utils import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        TODO Good
        """

        @functools.lru_cache(None)
        def getRobRecu(node):
            """
            return vals tuple ( with node,val without node)
            """
            if not node:
                return 0, 0
            left, right = getRobRecu(node.left), getRobRecu(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)

        return max(getRobRecu(root))


class Solution0:
    @functools.lru_cache(None)
    def rob(self, root: TreeNode) -> int:
        """初始版本"""
        if not root:
            return 0
        money_with_node = root.val
        if root.left:
            money_with_node += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money_with_node += self.rob(root.right.left) + self.rob(root.right.right)
        money_without_node = self.rob(root.left) + self.rob(root.right)
        return max(money_with_node, money_without_node)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            3,
            left=TreeNode(2, right=TreeNode(3)),
            right=TreeNode(3, right=TreeNode(1))
        ),
    ), 7],
    [dict(
        root=TreeNode(
            3,
            left=TreeNode(4, left=TreeNode(1), right=TreeNode(3)),
            right=TreeNode(5, right=TreeNode(1))
        ),
    ), 9],
])
def test_solutions(kw, expected):
    assert Solution().rob(**kw) == expected
    assert Solution0().rob(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
