#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 13:52:37
# @Last Modified : 2020-04-19 13:52:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def insertionSortListOrigin(self, head: ListNode) -> ListNode:
        # 找个排头 TODO
        dummy = ListNode(-1)
        pre = dummy
        # 依次拿head节点
        cur = head
        while cur:
            # 把下一次节点保持下来
            tmp = cur.next
            # 找到插入的位置
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # 进行插入操作
            cur.next = pre.next
            pre.next = cur
            pre= dummy
            cur = tmp
        return dummy.next

    def insertionSortList(self, head: ListNode) -> ListNode:
        """TODO"""
        if not (head and head.next):return head

        dummy = ListNode(None)
        dummy.next = head
        cur,sorted_tail = head.next,head

        while cur:
            prev = dummy
            while prev.next.val < cur.val:
                prev =prev.next
            if prev ==sorted_tail:
                cur,sorted_tail =cur.next,cur
            else:
                cur.next ,prev.next,sorted_tail.next = prev.next,cur,cur.next
                cur = sorted_tail.next
        return dummy.next








if __name__ == '__main__':
    sol = Solution()
    samples = [
        "4->2->1->3",
        # "-1->5->3->4->0",
        # "3"

    ]
    lists = [ListNode.init_list_from_str(x) for x in samples]
    # res = [sol.insertionSortList(x) for x in lists]
    res = [sol.insertionSortListOrigin(x) for x in lists]
    print(res)
