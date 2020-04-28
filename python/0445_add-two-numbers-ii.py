#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne
# @Created       : 2020-04-14 21:42:49
# @Last Modified : 2020-04-14 21:42:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
from common_utils import ListNode


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1,stack2 = [],[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        prev,head = None,None
        sum = 0
        while stack1 or stack2:
            sum //=10
            if stack1:
                sum+=stack1.pop()
            if stack2:
                sum+=stack2.pop()
            head = ListNode(sum%10)
            head.next = prev
            prev = head
        if sum>=10:
            head =ListNode(sum//10)
            head.next = prev
        return head



if __name__ == '__main__':
    sol = Solution()
    m = ListNode.init_list_from_str("7 -> 2 -> 4 -> 3")
    n = ListNode.init_list_from_str("5 -> 6 -> 4")

    res = sol.addTwoNumbers(m, n)
    print(res)