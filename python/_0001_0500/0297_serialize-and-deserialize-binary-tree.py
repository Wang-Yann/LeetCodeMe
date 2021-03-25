#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 14:38:05
# @Last Modified : 2020-04-22 14:38:05
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。
#
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。
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
#  提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
# 个问题。
#
#  说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
#  Related Topics 树 设计
#  👍 316 👎 0

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

