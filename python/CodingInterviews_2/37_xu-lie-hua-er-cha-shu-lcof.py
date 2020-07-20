#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 16:51:18
# @Last Modified : 2020-05-10 16:51:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请实现两个函数，分别用来序列化和反序列化二叉树。
#
#  示例:
#
#  你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
#
#  注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-b
# inary-tree/
#  Related Topics 树 设计
#  👍 46 👎 0


import pytest

from common_utils import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        """
        res = []

        def preOrder(root):
            if not root:
                res.append("#")
            else:
                res.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)

        preOrder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        """

        def helper(l):
            if l[0] == "#":
                l.pop(0)
                return None
            root = TreeNode(l.pop(0))
            root.left = helper(l)
            root.right = helper(l)
            return root

        return helper(data.split(","))


@pytest.mark.parametrize("root", [
    TreeNode(5,
             left=TreeNode(6),
             right=TreeNode(2, TreeNode(7), TreeNode(4))
             ),
    TreeNode(8)
])
def test_solutions(root):
    codec = Codec()
    res = codec.deserialize(codec.serialize(root))
    assert repr(res) == repr(root)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
