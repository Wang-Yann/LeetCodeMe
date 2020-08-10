#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 14:50:02
# @Last Modified : 2020-04-07 14:50:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

"""
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
#  示例：
#
#  给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
#  说明：
#
#  给定的 n 保证是有效的。
#
#  进阶：
#
#  你能尝试使用一趟扫描实现吗？
#  Related Topics 链表 双指针
#  👍 892 👎 0

"""
import pytest

from common_utils import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head
        first = dummy_head
        second = dummy_head
        # i=0
        # while i <=  n-1:
        #     i += 1
        #     first = first.next
        for i in range(1, n + 1):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        if second.next:
            second.next = second.next.next
        else:
            second.next = None
        return dummy_head.next


@pytest.mark.parametrize("kw,expected", [
    [dict(
        head=ListNode.init_list_from_str("1->2->3->4->5"),
        n=2
    ), ListNode.init_list_from_str("1->2->3->5")],
])
def test_solutions(kw, expected):
    assert repr(Solution().removeNthFromEnd(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
