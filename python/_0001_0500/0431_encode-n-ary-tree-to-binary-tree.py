#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 22:22:42
# @Last Modified : 2020-07-23 22:22:42
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 设计一个算法，可以将 N 叉树编码为二叉树，并能将该二叉树解码为原 N 叉树。一个 N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。类似地，一个二叉
# 树是指每个节点都有不超过 2 个孩子节点的有根树。你的编码 / 解码的算法的实现没有限制，你只需要保证一个 N 叉树可以编码为二叉树且该二叉树可以解码回原始 N
#  叉树即可。 
# 
#  例如，你可以将下面的 3-叉 树以该种方式编码： 
# 
#  
# 
#  
# 
#  
# 
#  注意，上面的方法仅仅是一个例子，可能可行也可能不可行。你没有必要遵循这种形式转化，你可以自己创造和实现不同的方法。 
# 
#  注意： 
# 
#  
#  N 的范围在 [1, 1000] 
#  不要使用类成员 / 全局变量 / 静态变量来存储状态。你的编码和解码算法应是无状态的。 
#  
#  Related Topics 树 
#  👍 15 👎 0

"""

import pytest

from common_utils import TreeNode, TreeNodeWithChildren as Node

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None

        rootNode = TreeNode(root.val)
        if len(root.children) > 0:
            firstChild = root.children[0]
            rootNode.left = self.encode(firstChild)

        # the parent for the rest of the children
        curr = rootNode.left

        # encode the rest of the children
        for i in range(1, len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right

        return rootNode

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        rootNode = Node(data.val, [])

        curr = data.left
        while curr:
            rootNode.children.append(self.decode(curr))
            curr = curr.right

        return rootNode


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    root = Node(val=1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
    coder = Codec()
    ss = coder.encode(root)
    # print(ss)
    assert repr(coder.decode(ss)) == repr(root)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
