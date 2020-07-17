#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 14:51:00
# @Last Modified : 2020-04-19 14:51:00
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
#  示例 1:
#
#  输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
#  示例 2:
#
#  输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#  Related Topics 排序 链表
#  👍 630 👎 0

from common_utils import ListNode


class Solution:

    def sortList(self, head: ListNode) -> ListNode:
        """ 归并排序"""
        if not (head and head.next):
            return head
        # fast, slow = head.next, head
        # while fast and fast.next:
        #     fast, slow = fast.next.next, slow.next
        # # TODO
        # mid, slow.next = slow.next, None
        fast, slow, prev = head, head, None
        while fast and fast.next:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None #Cut & save head

        print(head, slow)
        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)
        return self.mergeTwoLists(sorted_l1, sorted_l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next, cur, l2 = l2, l2, l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
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
    res = [sol.sortList(x) for x in lists]
    print(res)
