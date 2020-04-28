#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 23:35:43
# @Last Modified : 2020-04-10 23:35:43
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback

from common_utils import ListNode


class Solution:
    def isPalindromeS(self, head: ListNode) -> bool:
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur=cur.next
        return reversed(l)==l

    def isPalindromeSS(self, head: ListNode) -> bool:
        reverse,fast = None,head
        while fast and fast.next:
            fast=fast.next.next
            head.next, reverse, head = reverse, head, head.next
        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        print("Fast",fast)

        tail = head.next if fast else head
        print(head)
        print(reverse)
        print(tail)

        while reverse:
            if reverse.val != tail.val:
                return False
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()






if __name__ == '__main__':
    sol = Solution()
    sample0 = ListNode.init_list_from_str("1->2->3->4->5")
    sample1 = ListNode.init_list_from_str("1->2->3->2->1")
    sample2 = ListNode.init_list_from_str("1->2->3->3->2->1")
    print(sol.isPalindrome(sample0))
    print(sol.isPalindrome(sample1))
    print(sol.isPalindrome(sample2))
