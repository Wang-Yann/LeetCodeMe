#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:24:06
# @Last Modified : 2020-04-22 10:24:06
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给出一个完全二叉树，求出该树的节点个数。
#
#  说明：
#
#  完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为
# 第 h 层，则该层包含 1~ 2h 个节点。
#
#  示例:
#
#  输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6
#  Related Topics 树 二分查找
#  👍 193 👎 0
import pytest

from common_utils import TreeNode


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        ans = []
        if not root:
            return 0
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return len(ans)


class Solution1:

    def countNodes(self, root):
        """
        如果左右子树深度相同，那么说明右子数是满二叉树，左子树是完全二叉树
        """
        left_depth = self.get_depth(root, True)
        right_depth = self.get_depth(root, False)

        if left_depth == right_depth:
            return 2 ** left_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_depth(self, root, isLeft):
        if root is None:
            return 0
        if isLeft:
            return 1 + self.get_depth(root.left, isLeft)
        else:
            return 1 + self.get_depth(root.right, isLeft)


class Solution2:

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.right) + self.countNodes(root.left)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=TreeNode(
            1,
            left=TreeNode(2, TreeNode(4), TreeNode(5)),
            right=TreeNode(3, left=TreeNode(6))
        )
    ), 6],
])
def test_solutions(kw, expected):
    assert Solution().countNodes(**kw) == expected
    assert Solution1().countNodes(**kw) == expected
    assert Solution2().countNodes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
