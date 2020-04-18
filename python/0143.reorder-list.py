#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 22:53:30
# @Last Modified : 2020-04-18 22:53:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        TODO
        """
        if not (head and head.next):
            return
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, slow
        current, prev.next, prev = slow, None, None

        while current:
            current.next, prev, current = prev, current, current.next
        l1, l2 = head, prev

        dummy = ListNode(-1)
        current = dummy
        while l1 and l2:
            current.next=l1
            current=l1
            l1 =l1.next
            # print(dummy,current, l1, l2, sep="\t")

            current.next, current, l2 = l2, l2, l2.next
            # print(dummy, current, l1, l2, sep="\t")

        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "1->2->3->4->5->6",
        "1->2->3->4->5",
    ]
    lists = [ListNode.init_list_from_str(x) for x in samples]
    res = [sol.reorderList(x) for x in lists]
    print(lists)
