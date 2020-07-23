#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 21:23:46
# @Last Modified : 2020-07-23 21:23:46
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 序列化是指将一个数据结构转化为位序列的过程，因此可以将其存储在文件中或内存缓冲区中，以便稍后在相同或不同的计算机环境中恢复结构。 
# 
#  设计一个序列化和反序列化 N 叉树的算法。一个 N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。序列化 / 反序列化算法的算法实现没有限制。你只需
# 要保证 N 叉树可以被序列化为一个字符串并且该字符串可以被反序列化成原树结构即可。 
# 
#  例如，你需要序列化下面的 3-叉 树。 
# 
#  
# 
#  
# 
#  
# 
#  为 [1 [3[5 6] 2 4]]。你不需要以这种形式完成，你可以自己创造和实现不同的方法。 
# 
#  
# 
#  注意： 
# 
#  
#  N 的范围在 [1, 1000] 
#  不要使用类成员 / 全局变量 / 静态变量来存储状态。你的序列化和反序列化算法应是无状态的。 
#  
#  Related Topics 树 
#  👍 24 👎 0

"""

import pytest

from common_utils import TreeNodeWithChildren as Node

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:

    def dfs(self, root):
        ans = ""
        if root is None:
            return ans
        ans += "["
        ans += str(root.val)
        N = len(root.children or [])
        for i in range(N):
            ans += self.dfs(root.children[i])
        ans += "]"
        return ans

    def solve(self, data):
        num = 0
        while data[self.pos].isdigit():
            num *= 10
            num += ord(data[self.pos]) - ord('0')
            self.pos += 1
        node = Node(num, [])
        while self.pos < len(data):
            if data[self.pos] == '[':
                self.pos += 1
                node.children.append(self.solve(data))
            elif data[self.pos] == ']':
                self.pos += 1
                return node

    def serialize(self, root: 'Node') -> str:
        ans = ""
        if root is None:
            return ans
        return self.dfs(root)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        self.pos = 1
        return self.solve(data)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)


class Codec1:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            res.append(str(len(node.children or [])))
            if node.children:
                for child in node.children:
                    dfs(child)

        dfs(root)
        # print(res)
        return "#".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data = iter(data.split("#"))

        def helper():
            root = Node(int(next(data)), [])
            num = int(next(data))
            for _ in range(num):
                root.children.append(helper())
            return root

        return helper()


def test_solution():
    root = Node(val=1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
    coder = Codec()
    ss = coder.serialize(root)
    print(ss)
    assert repr(coder.deserialize(ss)) == repr(root)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
