#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne
# @Created       : 2020-04-14 21:42:49
# @Last Modified : 2020-04-14 21:42:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
#  你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
#  进阶：
#
#  如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
#
#
#  示例：
#
#  输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
#
#  Related Topics 链表
#  👍 237 👎 0

"""
import pytest

from common_utils import ListNode


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        prev, head = None, None
        sum = 0
        while stack1 or stack2:
            sum //= 10
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()
            head = ListNode(sum % 10)
            head.next = prev
            prev = head
        if sum >= 10:
            head = ListNode(sum // 10)
            head.next = prev
        return head


@pytest.mark.parametrize("kw,expected", [
    [dict(
        l1=ListNode.init_list_from_str("7 -> 2 -> 4 -> 3"),
        l2=ListNode.init_list_from_str("5 -> 6 -> 4")
    ), ListNode.initList([7, 8, 0, 7])],
])
def test_solutions(kw, expected):
    assert repr(Solution().addTwoNumbers(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
