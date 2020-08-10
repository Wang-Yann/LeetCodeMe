#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-17 16:16:28
# @Last Modified : 2020-04-17 16:16:28
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
"""
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
#  示例：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  Related Topics 链表
#  👍 1152 👎 0

"""
import pytest

from common_utils import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(-1)
        cur_head = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                cur_head.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur_head.next = l2
                l2 = l2.next
            cur_head = cur_head.next
        while l1:
            cur_head.next = l1
            l1 = l1.next
            cur_head = cur_head.next
        while l2:
            cur_head.next = l2
            l2 = l2.next
            cur_head = cur_head.next
        return dummyHead.next


@pytest.mark.parametrize("kw,expected", [
    [dict(
        l1=ListNode.init_list_from_str("1->2->4"),
        l2=ListNode.init_list_from_str("1->3->4")
    ), ListNode.initList([1, 1, 2, 3, 4, 4])],
])
def test_solutions(kw, expected):
    assert repr(Solution().mergeTwoLists(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
