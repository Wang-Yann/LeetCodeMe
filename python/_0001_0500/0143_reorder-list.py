#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 22:53:30
# @Last Modified : 2020-04-18 22:53:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  示例 1:
#
#  给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
#  示例 2:
#
#  给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#  Related Topics 链表
#  👍 253 👎 0

"""
import copy

import pytest

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
            current.next = l1
            current = l1
            l1 = l1.next
            # print(dummy,current, l1, l2, sep="\t")

            current.next, current, l2 = l2, l2, l2.next
            # print(dummy, current, l1, l2, sep="\t")

        # return dummy.next


class Solution1:

    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None


@pytest.mark.parametrize("args,expected", [
    (
            ListNode.init_list_from_str("1->2->3->4"),
            ListNode.init_list_from_str("1->4->2->3"),
    ),
    (
            ListNode.init_list_from_str("1->2->3->4->5"),
            ListNode.init_list_from_str("1->5->2->4->3"),
    ),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(args, expected, SolutionCLS):
    h = copy.deepcopy(args)
    SolutionCLS().reorderList(h)
    assert repr(h) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
