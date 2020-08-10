#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-17 17:02:20
# @Last Modified : 2020-04-17 17:02:20
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

"""
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例:
#
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#  Related Topics 链表
#  👍 552 👎 0

"""
import copy

import pytest

from common_utils import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """ME"""
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


class Solution1:
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


class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
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
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node


@pytest.mark.parametrize("CLS", [
    Solution, Solution1, Solution2
])
@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([1, 2, 3, 4]), ListNode.initList([2, 1, 4, 3]))
])
def test_solutions(CLS, args, expected):
    assert repr(CLS().swapPairs(copy.deepcopy(args))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
