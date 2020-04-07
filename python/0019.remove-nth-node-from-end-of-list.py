#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 14:50:02
# @Last Modified : 2020-04-07 14:50:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from common_utils import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head
        first = dummy_head
        second = dummy_head
        # i=0
        # while i <=  n-1:
        #     i += 1
        #     first = first.next
        for i in range(1,n+1):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        if second.next:
            second.next=second.next.next
        else:
            second.next=None
        return dummy_head.next


if __name__ == '__main__':
    # 1->2->3->4->5, 和 n = 2
    sol = Solution()
    sample = ListNode.init_list_from_str("1->2->3->4->5")
    print(sol.removeNthFromEnd(sample, 2))
    # print(sol.removeNthFromEnd(sample, 1))
