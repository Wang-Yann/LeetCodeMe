#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 12:25:29
# @Last Modified : 2020-04-19 12:25:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from collections import defaultdict

from common_utils import Node


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        clone = defaultdict(lambda:Node(0))
        clone[None] = None
        cur = head
        while cur:
            clone[cur].val = cur.val
            clone[cur].next = clone[cur.next]
            clone[cur].random = clone[cur.random]
            cur = cur.next
        return clone[head]

    def copyRandomList2(self, head):
        dummy = Node(0)
        current, prev, copies = head, dummy, {}

        while current:
            copied = Node(current.val)
            copies[current] = copied
            prev.next = copied
            prev, current = prev.next, current.next

        current = head
        while current:
            if current.random:
                copies[current].random = copies[current.random]
            current = current.next

        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
        []
    ]
    lists = [Node.initList(x) for x in samples]
    print(lists)
    # res = [sol.copyRandomList(x) for x in lists]
    res = [sol.copyRandomList2(x) for x in lists]

    print(res)
