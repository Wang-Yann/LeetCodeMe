#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 16:27:07
# @Last Modified : 2020-04-19 16:27:07
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def reverseListIter(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = head
        while cur:
            dummy.next, cur.next, cur = cur, dummy.next, cur.next
        return dummy.next

    def reverseListIter1(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reverseListRecurse(self, head: ListNode) -> ListNode:
        """TODO
        涉及到链表的操作，一定要在纸上把过程先画出来，再写程序
        https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode/
        假设列表的其余部分已经被反转，现在我该如何反转它前面的部分
        如 N1->N2->..->Nk->N(k+1)<-..<-Nm<- ∅
        我们正处于Nk
        所以
        Nk.next.next=Nk

        """
        if not (head and head.next):
            return head
        p = self.reverseListRecurse(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "1->2->3->4->5",
        "1->2",
        "1"
    ]
    # res = [ sol.reverseList(ListNode.init_list_from_str(x)) for x in samples]
    # res = [ sol.reverseListIter1(ListNode.init_list_from_str(x)) for x in samples]
    res = [sol.reverseListRecurse(ListNode.init_list_from_str(x)) for x in samples]
    print(res)
