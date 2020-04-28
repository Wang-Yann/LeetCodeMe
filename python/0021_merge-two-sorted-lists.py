#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-17 16:16:28
# @Last Modified : 2020-04-17 16:16:28
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        cur_head = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                cur_head.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur_head.next = l2
                l2 = l2.next
            cur_head = cur_head.next
        while l1:
            cur_head.next = l1
            l1 = l1.next
            cur_head = cur_head.next
        while l2:
            cur_head.next = l2
            l2 = l2.next
            cur_head = cur_head.next
        return dummyHead.next


if __name__ == '__main__':
    sol = Solution()
    s1 = ListNode.init_list_from_str("1->2->4")
    s2 = ListNode.init_list_from_str("1->3->4")
    res = sol.mergeTwoLists(s1, s2)
    print(res)
