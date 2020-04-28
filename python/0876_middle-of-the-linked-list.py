#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 22:58:07
# @Last Modified : 2020-04-19 22:58:07
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def middleNode(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6]
    ]
    lists = [ListNode.initList(x) for x in samples]
    res = [sol.middleNode(x) for x in lists]
    print(res)
