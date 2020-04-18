#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 20:29:48
# @Last Modified : 2020-04-18 20:29:48
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def reverseBetweenMe(self, head: ListNode, m: int, n: int) -> ListNode:
        i = 0
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while i < m - 1:
            cur = cur.next
            i += 1
        left_end = cur
        mid_stack = []
        while i < n:
            cur = cur.next
            mid_stack.append(ListNode(cur.val))
            i += 1
        right_part = cur.next
        for node in mid_stack[::-1]:
            left_end.next = node
            left_end = left_end.next
        left_end.next = right_part
        return dummy.next

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        diff, dummy, cur = n - m + 1, ListNode(-1), head
        dummy.next = head

        last_unswap = dummy
        while cur and m > 1:
            cur, last_unswap, m = cur.next, cur, m - 1
        prev, first_swap = last_unswap, cur
        print(first_swap, last_unswap, sep="\t")
        print(cur, prev, sep="\t")
        # Reverse List part
        while cur and diff > 0:
            prev, cur.next, cur, diff = cur, prev, cur.next, diff - 1
        print(cur.val, prev.val, sep="\t")
        print(first_swap.val, last_unswap.val, sep="\t")

        first_swap.next, last_unswap.next = cur, prev

        return dummy.next

    def reverseList(self, head):
        """
        TODO
        """
        dummy = ListNode(-1)
        while head:
            print("Before", head, dummy.next, head.next, sep="\t")
            dummy.next, head.next, head = head, dummy.next, head.next
            # print("After",dummy.next, head.next, head,sep="\t")
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("1->2->3->4->5", 2, 4),
        # ("1->2->3->4->5", 2, 2),
        # ("1", 1, 1),
    ]
    res = [sol.reverseBetween(ListNode.init_list_from_str(x), m, n) for x, m, n in samples]
    # res = [sol.reverseList(ListNode.init_list_from_str(x)) for x, m, n in samples]
    print(res)
