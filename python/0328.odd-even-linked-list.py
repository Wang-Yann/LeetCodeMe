#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 17:00:02
# @Last Modified : 2020-04-19 17:00:02
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        TODO
        https://leetcode-cn.com/problems/odd-even-linked-list/solution/qi-ou-lian-biao-by-leetcode/
        我们用变量 head 和 odd_tail 保存奇链表的头和尾指针。 even_head 和 cur 保存偶链表的头和尾指针
        """
        if not (head and head.next):
            return head
        odd_tail, even, even_head = head, head.next, head.next
        while even and even.next:
            odd_tail.next = even.next
            odd_tail = odd_tail.next
            even.next = odd_tail.next
            even = even.next
        odd_tail.next = even_head
        return head


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "1->2->3->4->5",
        # "2->1->3->5->6->4->7",
    ]
    lists = [ListNode.init_list_from_str(x) for x in samples]
    res = [sol.oddEvenList(x) for x in lists]
    print(res)
