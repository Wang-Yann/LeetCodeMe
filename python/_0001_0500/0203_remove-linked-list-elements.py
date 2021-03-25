#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 15:46:25
# @Last Modified : 2020-04-19 15:46:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 删除链表中等于给定值 val 的所有节点。
#
#  示例:
#
#  输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#
#  Related Topics 链表
#  👍 408 👎 0
import copy

import pytest

from common_utils import ListNode


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """Me"""
        if not head:
            return head
        dummy = ListNode(None)
        cur, prev = head, dummy
        while cur:
            while cur and cur.val == val:
                cur = cur.next
            prev.next = cur
            prev = prev.next
            if not cur:
                break
            cur = cur.next
        return dummy.next


class Solution1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        cur, prev = head, dummy
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next


@pytest.mark.parametrize("args,expected", [
    [(ListNode.init_list_from_str("1->2->6->3->4->5->6"), 6), ListNode.initList([1, 2, 3, 4, 5])],
    [(ListNode.init_list_from_str("1->2->6->3->4"), 6), ListNode.initList([1, 2, 3, 4])],
    [(ListNode.init_list_from_str("1->2->3->4"), 6), ListNode.initList([1, 2, 3, 4])]
])
def test_solutions(args, expected):
    assert repr(Solution().removeElements(*copy.deepcopy(args))) == repr(expected)
    assert repr(Solution1().removeElements(*copy.deepcopy(args))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
