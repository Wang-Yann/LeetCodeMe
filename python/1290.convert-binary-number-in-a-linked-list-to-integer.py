#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 00:35:29
# @Last Modified : 2020-04-20 00:35:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def getDecimalValueMe(self, head: ListNode) -> int:
        if not head:
            return None
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)

    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [1, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0],
        [1],
        [0, 0],
        [0, 0, 1, 1],
        []
    ]
    lists = [ListNode.initList(x) for x in samples]
    res = [sol.getDecimalValue(x) for x in lists]
    print(res)
