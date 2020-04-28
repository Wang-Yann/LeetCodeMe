#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 15:46:25
# @Last Modified : 2020-04-19 15:46:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def removeElementsMe(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(None)
        cur, prev = head, dummy
        while cur:
            while cur and cur.val == val:
                cur =cur.next
            prev.next = cur
            prev = prev.next
            if not cur:
                break
            cur = cur.next
        return dummy.next

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next=head
        cur, prev = head, dummy
        while cur:
            if cur.val == val:
                prev.next =cur.next
            else:
                prev=cur
            cur=cur.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("1->2->6->3->4->5->6", 6),
        ("1->2->6->3->4", 6),
        ("1->2->3->4", 6),
    ]
    lists = [(ListNode.init_list_from_str(x), y) for x, y in samples]
    res = [sol.removeElements(*x) for x in lists]
    print(res)
