#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 10:52:18
# @Last Modified : 2020-04-18 10:52:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
#  示例 1:
#
#  输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
#  示例 2:
#
#  输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#  Related Topics 链表 双指针
#  👍 293 👎 0

"""
import copy

import pytest

from common_utils import ListNode


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """Me"""
        if not head or not k:
            return head
        cur_head = head
        l = 1
        while head.next:
            head = head.next
            l += 1
        tail = head
        k = k % l
        if k == 0:
            return cur_head
        # print(cur_head,tail,l,k)
        cnt = l - k
        while cnt > 0:
            tmp = cur_head
            cur_head = cur_head.next
            tmp.next = None
            tail.next = tmp
            tail = tail.next
            cnt -= 1
        return cur_head


class Solution1:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if not head or not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head


@pytest.mark.parametrize("args,expected", [
    [(ListNode.initList([1, 2, 3, 4, 5]), 2), ListNode.initList([4, 5, 1, 2, 3])],
    [(ListNode.initList([0, 1, 2]), 4), ListNode.initList([2, 0, 1])],
    [(ListNode.initList([1, 2]), 2), ListNode.initList([1, 2])],
])
def test_solutions(args, expected):
    assert repr(Solution().rotateRight(*copy.deepcopy(args))) == repr(expected)
    assert repr(Solution1().rotateRight(*args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
