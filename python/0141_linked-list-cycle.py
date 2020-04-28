#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 13:30:44
# @Last Modified : 2020-04-19 13:30:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from common_utils import ListNode


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        if not head:return False
        fast  = head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1)
    ]
    res = [sol.hasCycle(ListNode.initList(x)) for x in samples]
    print(res)
