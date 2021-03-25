#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20

"""
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#  示例：
#
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#  Related Topics 链表 数学
#  👍 4611 👎 0

"""

# Definition for singly-linked list.
import pytest

from common_utils import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1stack, l2stack = [], []
        while l1:
            l1stack.append(l1.val)
            l1 = l1.next
        while l2:
            l2stack.append(l2.val)
            l2 = l2.next
        len1, len2 = len(l1stack), len(l2stack)
        if len1 >= len2:
            long, short = l1stack, l2stack
        else:
            short, long = l1stack, l2stack
        i = 0
        carry = 0
        head_node, cur_node = None, None
        while i < len(short):
            v_sum = short[i] + long[i] + carry
            if v_sum >= 10:
                carry = 1
                v_sum = v_sum - 10
            else:
                carry = 0
            if not head_node:
                cur_node = ListNode(v_sum)
                head_node = cur_node
            else:
                next_node = ListNode(v_sum)
                cur_node.next = next_node
                cur_node = next_node

            i += 1
        while i < len(long):
            v_sum = long[i] + carry
            if v_sum >= 10:
                carry = 1
                v_sum = v_sum - 10
            else:
                carry = 0
            next_node = ListNode(v_sum)
            cur_node.next = next_node
            cur_node = next_node
            i += 1
        if carry:
            next_node = ListNode(carry)
            cur_node.next = next_node
        return head_node


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head_node = ListNode(0)
        curr_node = head_node

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            v_sum = x + y + carry
            carry = v_sum // 10
            curr_node.next = ListNode(v_sum % 10)
            curr_node = curr_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr_node.next = ListNode(1)
        return head_node.next


@pytest.mark.parametrize("kw,expected", [
    [dict(
        l1=ListNode.initList([2, 4, 3]),
        l2=ListNode.initList([5, 6, 4])
    ), ListNode.initList([7, 0, 8])],
])
def test_solutions(kw, expected):
    assert repr(Solution().addTwoNumbers(**kw)) == repr(expected)
    assert repr(Solution1().addTwoNumbers(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
