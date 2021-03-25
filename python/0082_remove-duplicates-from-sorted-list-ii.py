#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 13:08:39
# @Last Modified : 2020-04-18 13:08:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
#  示例 1:
#
#  输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
#  示例 2:
#
#  输入: 1->1->1->2->3
# 输出: 2->3
#  Related Topics 链表
#  👍 319 👎 0

"""
import copy

import pytest

from common_utils import ListNode


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        pre.next = None
        return dummy.next


class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 2, 3, 3, 4, 4, 5])), ListNode.initList([1, 2, 5])],
    [dict(head=ListNode.initList([1, 1, 1, 2, 3])), ListNode.initList([2, 3])],
    [dict(head=ListNode.initList([3, 1, 1, 1, 2, 2, 2])), ListNode.initList([3])],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert repr(SolutionCLS().deleteDuplicates(**copy.deepcopy(kw))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
