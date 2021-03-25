#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-21 21:08:59
# @Last Modified : 2020-04-21 21:08:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
#  struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
#  初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
#  示例：
#
#
#
#  输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"ri
# ght":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right
# ":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left"
# :null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":nu
# ll,"next":null,"right":null,"val":7},"val":3},"val":1}
#
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4
# ","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next"
# :null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":
# null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":
# "6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"va
# l":1}
#
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#
#
#
#
#  提示：
#
#
#  你只能使用常量级额外空间。
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#  Related Topics 树 深度优先搜索
#  👍 207 👎 0
import copy

import pytest

from common_utils import TreeNodeWithNext as Node


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        """Me"""
        if not root:
            return root
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length - 1):
                queue[i].next = queue[i + 1]
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            cur = head
            while cur and cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            head = head.left
        return root


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        """
        Good
        """
        if not root: return root
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


@pytest.mark.parametrize("args,expected", [
    [Node(1, Node(2, Node(4), Node(5), None), Node(3, Node(6), Node(7), None), None),
     [1, 2, 3, 4, 5, 6, 7]]
])
def test_solutions(args, expected):
    assert repr(Solution().connect(copy.deepcopy(args))) == repr(expected)
    assert repr(Solution1().connect(copy.deepcopy(args))) == repr(expected)
    assert repr(Solution2().connect(copy.deepcopy(args))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
