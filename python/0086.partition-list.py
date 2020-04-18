#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 19:21:33
# @Last Modified : 2020-04-18 19:21:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


from common_utils import ListNode


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        right_dummy = ListNode(-1)
        cur = dummy
        right_cur = right_dummy
        while head:
            if head.val < x:
                cur.next = head
                cur = head
            else:
                right_cur.next = head
                right_cur = right_cur.next
            head = head.next
        right_cur.next = None
        cur.next = right_dummy.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ("1->4->3->2->5->2", 3),
        ("1", 3)

    ]
    res = [sol.partition(ListNode.init_list_from_str(head), x) for (head, x) in samples]
    print(res)
