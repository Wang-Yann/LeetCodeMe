#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 13:08:39
# @Last Modified : 2020-04-18 13:08:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        left = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = cur.next
            else:
                left.next = cur
                left = cur
                cur = cur.next
        left.next = None
        return dummy.next



if __name__ == '__main__':
    sol = Solution()
    samples = [
        "1->2->3->3->4->4->5",
        "1->1->1->2->3",
        "1"
    ]
    res = [sol.deleteDuplicates(ListNode.init_list_from_str(x)) for x in samples]
    print(res)
