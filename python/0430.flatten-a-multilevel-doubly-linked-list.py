#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 17:28:46
# @Last Modified : 2020-04-19 17:28:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import DoubleWithChildNode as Node


class SolutionMe:

    def flatten(self, head: 'Node') -> 'Node':
        """ 题意容易混淆"""
        if not head:
            return head
        node_list = []
        self.dfs(head, node_list)
        print([x.val for x in node_list])
        length = len(node_list)
        for i in range(length):
            if i <= length - 2:
                node_list[i].next = node_list[i + 1]
            if i >= 1:
                node_list[i].prev = node_list[i - 1]
        return node_list[0]

    def dfs(self, head, node_list):
        if not head or head.val is None:
            return
        node_list.append(Node(head.val))
        if head.child:
            cld = head.child
            head.child = None
            self.dfs(cld, node_list)
        self.dfs(head.next, node_list)


class SolutionRec(object):

    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next

    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)


class Solution(object):
    """
       方法二：迭代的深度优先搜索

       """

    def flatten(self, head):
        if not head:
            return

        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [[1, 2, 3, 4, 5, 6],
         [None, None, 7, 8, 9, 10],
         [None, None, None, 11, 12]],
        [[1],
         [2],
         [3]],
        # []
    ]
    lists = [Node.initList(x) for x in samples]
    # print(lists)
    res = [sol.flatten(x) for x in lists]
    print(res)
