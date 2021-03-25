#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 19:21:33
# @Last Modified : 2020-04-18 19:21:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
#  你应当保留两个分区中每个节点的初始相对位置。
#
#  示例:
#
#  输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#
#  Related Topics 链表 双指针
#  👍 224 👎 0

"""
import pytest

from common_utils import ListNode


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        right_dummy = ListNode(-1)
        cur = dummy
        right_cur = right_dummy
        while head:
            if head.val < x:
                cur.next = head
                cur = head
            else:
                right_cur.next = head
                right_cur = right_cur.next
            head = head.next
        right_cur.next = None
        cur.next = right_dummy.next
        return dummy.next


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 4, 3, 2, 5, 2]), x=3), ListNode.initList([1, 2, 2, 4, 3, 5])],
])
def test_solutions(kw, expected):
    assert repr(Solution().partition(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
