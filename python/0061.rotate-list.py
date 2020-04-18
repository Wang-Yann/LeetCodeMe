#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 10:52:18
# @Last Modified : 2020-04-18 10:52:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def rotateRightMe(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        cur_head = head
        l = 1
        while head.next:
            head = head.next
            l += 1
        tail = head
        k = k % l
        if k == 0:
            return cur_head
        # print(cur_head,tail,l,k)
        cnt = l - k
        while cnt > 0:
            tmp = cur_head
            cur_head = cur_head.next
            tmp.next = None
            tail.next = tmp
            tail = tail.next
            cnt -= 1
        return cur_head

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if not head or not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head



if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("1->2->3->4->5", 2),
        ("0->1->2", 4),
        ("1->2", 2)

    ]
    res = [sol.rotateRight(ListNode.init_list_from_str(head), k) for head, k in samples]
    for x in res:
        print(x)
