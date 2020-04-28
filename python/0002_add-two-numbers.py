#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "Node:{0.val}".format(self)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1stack, l2stack = [], []
        while l1:
            l1stack.append(l1.val)
            l1 = l1.next
        while l2:
            l2stack.append(l2.val)
            l2 = l2.next
        len1, len2 = len(l1stack), len(l2stack)
        if len1 >= len2:
            long, short = l1stack, l2stack
        else:
            short, long = l1stack, l2stack
        i = 0
        carry = 0
        head_node, cur_node = None, None
        while i < len(short):
            v_sum = short[i] + long[i] + carry
            if v_sum >= 10:
                carry = 1
                v_sum = v_sum - 10
            else:
                carry = 0
            if not head_node:
                cur_node = ListNode(v_sum)
                head_node = cur_node
            else:
                next_node = ListNode(v_sum)
                cur_node.next = next_node
                cur_node = next_node

            i += 1
        while i < len(long):
            v_sum = long[i] + carry
            if v_sum >= 10:
                carry = 1
                v_sum = v_sum - 10
            else:
                carry = 0
            next_node = ListNode(v_sum)
            cur_node.next = next_node
            cur_node = next_node
            i += 1
        if carry:
            next_node = ListNode(carry)
            cur_node.next = next_node
        return head_node

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head_node = ListNode(0)
        curr_node = head_node

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else  0
            v_sum = x + y + carry
            carry = v_sum // 10
            curr_node.next = ListNode(v_sum % 10)
            curr_node = curr_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr_node.next = ListNode(1)
        return head_node.next


if __name__ == '__main__':
    sol = Solution()
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    m1 = ListNode(5)
    m2 = ListNode(6)
    m3 = ListNode(4)
    m1.next = m2
    m2.next = m3

    print(m1, n1)
    res = sol.addTwoNumbers2(m1, n1)
    while res:
        print(res.val)
        res = res.next
        print("-->")
