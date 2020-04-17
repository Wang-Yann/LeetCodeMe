#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-17 17:02:20
# @Last Modified : 2020-04-17 17:02:20
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:
    def swapPairsMe(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        dummy = ListNode(-1)
        cur_head = dummy
        while head and head.next:
            now_tail = head.next.next
            cur_pre = head.next

            head.next = now_tail
            cur_pre.next = head

            cur_head.next = cur_pre
            cur_head = cur_head.next.next
            head = cur_pre.next.next
        return dummy.next

    def swapPairs(self, head: ListNode) -> ListNode:
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


    def swapPairsRecurse(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node



if __name__ == '__main__':
    sol = Solution()
    sample = [
        "1->2->3->4",
        "1->3->4",
        "2->6",
        "1",
        ""
    ]
    s_list = [ListNode.init_list_from_str(x) for x in sample]
    # for res in [sol.swapPairs(x) for x in s_list]:
    for res in [sol.swapPairsRecurse(x) for x in s_list]:
        print(res)
