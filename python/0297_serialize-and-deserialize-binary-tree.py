#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 14:38:05
# @Last Modified : 2020-04-22 14:38:05
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

"""
import pickle
data=pickle.dumps(root)
root=pickle.loads(data)

"""
import pytest

from common_utils import TreeNode


class Codec:
    """
    层/先序遍历OK
    但是None要补全
    """

    # def preOrderTraversal(root, s):
    #     if not root:
    #         s += "None,"
    #     else:
    #         s += str(root.val) + ","
    #         s = preOrderTraversal(root.left, s)
    #         s = preOrderTraversal(root.right, s)
    #     return s
    #
    # return preOrderTraversal(root, "")

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        results = []

        def preOrderTraversal(root):
            if not root:
                results.append("None")
            else:
                results.append(str(root.val))
                preOrderTraversal(root.left)
                preOrderTraversal(root.right)

        preOrderTraversal(root)
        return ",".join(results)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rebuild(l):
            if l[0] == "None":
                l.pop(0)
                return None
            root = TreeNode(l.pop(0))
            root.left = rebuild(l)
            root.right = rebuild(l)
            return root

        data_list = data.split(",")
        return rebuild(data_list)


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
    assert repr(res)==repr(root)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

