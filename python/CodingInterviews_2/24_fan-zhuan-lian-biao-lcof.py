#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 23:55:50
# @Last Modified : 2020-04-26 23:55:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
#
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 5000
#
#
#
#  注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
#  Related Topics 链表
#  👍 67 👎 0
import copy

import pytest

from common_utils import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = head
        while cur:
            dummy.next, cur.next, cur = cur, dummy.next, cur.next
        return dummy.next


class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 2, 3, 4, 5])), ListNode.initList([5, 4, 3, 2, 1])],
])
def test_solutions(kw, expected):
    kw1 = copy.deepcopy(kw)
    assert repr(Solution().reverseList(**kw)) == repr(expected)
    assert repr(Solution1().reverseList(**kw1)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
