#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 17:17:38
# @Last Modified : 2020-07-29 17:17:38
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一棵二叉搜索树和其中的一个节点 node ，找到该节点在树中的中序后继。 
# 
#  如果节点没有中序后继，请返回 null 。 
# 
#  一个结点 node 的中序后继是键值比 node.val大所有的结点中键值最小的那个。 
# 
#  你可以直接访问结点，但无法直接访问树。每个节点都会有其父节点的引用。节点定义如下： 
# 
#  class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# } 
# 
#  
# 
#  进阶： 
# 
#  你能否在不访问任何结点的值的情况下解决问题? 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  输入: tree = [2,1,3], node = 1
# 输出: 2
# 解析: 1 的中序后继结点是 2 。注意节点和返回值都是 Node 类型的。
#  
# 
#  示例 2: 
# 
#  
# 
#  输入: tree = [5,3,6,2,4,null,null,1], node = 6
# 输出: null
# 解析: 该结点没有中序后继，因此返回 null 。
#  
# 
#  示例 3: 
# 
#  
# 
#  输入: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,
# null,9], node = 15
# 输出: 17
#  
# 
#  示例 4: 
# 
#  
# 
#  输入: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,
# null,9], node = 13
# 输出: 15
#  
# 
#  
# 
#  提示： 
# 
#  
#  -10^5 <= Node.val <= 10^5 
#  1 <= Number of Nodes <= 10^4 
#  树中各结点的值均保证唯一。 
#  
#  Related Topics 树 
#  👍 20 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return "{}[{},{}]".format(self.val, repr(self.left), repr(self.right))


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        """
        若 node 结点有右孩子，则它的后继在树中相对较低的位置。我们向右走一次，再尽可能的向左走，返回最后所在的结点。
        若 node 结点没有右孩子，则它的后继在树中相对较高的位置。我们向上走到直到结点 tmp 的左孩子是 node 的父节点时，则 node 的后继为 tmp。

        """
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        # the successor is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent


# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    node2 = Node(2)
    node1 = Node(1)
    node3 = Node(3)
    node2.left = node1
    node2.right = node3
    node1.parent = node2
    node3.parent = node2
    assert repr(Solution().inorderSuccessor(node1).val) == repr(node2.val)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
