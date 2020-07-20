#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 23:42:39
# @Last Modified : 2020-05-04 23:42:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
# 它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
#
#
#
#  示例：
#
#  给定一个链表: 1->2->3->4->5, 和 k = 2.
#
# 返回链表 4->5.
#  Related Topics 链表 双指针
#  👍 57 👎 0


import pytest

from common_utils import ListNode


class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """没有 kk 大于链表长度的 case ，因此不用考虑越界问题"""
        prev, later = head, head
        for _ in range(k):
            prev = prev.next
        while prev:
            prev, later = prev.next, later.next
        return later


@pytest.mark.parametrize("args,expected", [
    ([ListNode.init_list_from_str("1->2->3->4->5"), 2], ListNode.initList([4, 5])),
])
def test_solutions(args, expected):
    res = Solution().getKthFromEnd(*args)
    while res and expected:
        assert res.val == expected.val
        res, expected = res.next, expected.next
    assert res is None and expected is None


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
