#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 13:30:44
# @Last Modified : 2020-04-19 13:30:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from common_utils import ListNode


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1)
    ]
    res = [sol.detectCycle(ListNode.initList(x)) for x in samples]
    print(res)
