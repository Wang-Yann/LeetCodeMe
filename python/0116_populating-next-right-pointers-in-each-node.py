#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-21 21:08:59
# @Last Modified : 2020-04-21 21:08:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNodeWithNext as Node


class Solution:

    def connectMe(self, root: 'Node') -> 'Node':
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

    def connect1(self, root: 'Node') -> 'Node':
        head = root
        while head:
            cur = head
            while cur and cur.left:
                cur.left.next=cur.right
                if cur.next:
                    cur.right.next=cur.next.left
                cur = cur.next
            head=head.left
        return root

    def connect(self, root: 'Node') -> 'Node':
        """
        Good
        """
        if not root:return root
        if root.left:
            root.left.next =root.right
        if root.right and root.next:
            root.right.next =root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        Node(1, Node(2, Node(4), Node(5), None), Node(3, Node(6), Node(7), None), None)
    ]
    res = [sol.connect(x) for x in samples]
    print(samples)
