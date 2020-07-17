#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 17:40:36
# @Last Modified : 2020-04-22 17:40:36
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
#
#  设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化
# 为最初的二叉搜索树。
#
#  编码的字符串应尽可能紧凑。
#
#  注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
#  Related Topics 树
#  👍 91 👎 0

"""

from common_utils import TreeNode


class CodecMe:
    """
    二叉搜索树能只够通过前序序列或后序序列构造，是因为以下两个因素：
        二叉树可以通过前序序列或后序序列和中序序列构造。
        二叉搜索树的中序序列是递增排序的序列，inorder = sorted(preorder)

    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        照常前序遍历
        """
        res = []
        stack = [root]
        if not root: return "#"
        while stack:
            cur = stack.pop()
            if cur:
                res.append(str(cur.val))
                stack.append(cur.right)
                stack.append(cur.left)
            else:
                res.append("#")
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        data_list = data.split(",")

        def buildPreOrder():
            val = data_list.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = buildPreOrder()
            node.right = buildPreOrder()
            return node

        return buildPreOrder()


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        """

        def gen_preorder(node):
            if not node:
                yield '#'
            else:
                yield str(node.val)
                yield from gen_preorder(node.left)
                yield from gen_preorder(node.right)

        return ','.join(gen_preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        chunk_iter = iter(data.split(","))

        def builder():
            val = next(chunk_iter)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = builder()
            node.right = builder()
            return node

        # https://stackoverflow.com/a/42373311/568901
        return builder()


if __name__ == '__main__':
    samples = [
        TreeNode(8,
                 left=TreeNode(1),
                 right=TreeNode(10, TreeNode(9), TreeNode(12))
                 ),
        TreeNode(12),
        None

    ]
    for root in samples:
        codec = Codec()
        data = codec.serialize(root)
        print(data)
        res = codec.deserialize(data)
        print(res)
