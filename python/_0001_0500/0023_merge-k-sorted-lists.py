#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-17 16:16:28
# @Last Modified : 2020-04-17 16:16:28
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

"""
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
#  示例:
#
#  输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#  Related Topics 堆 链表 分治算法
#  👍 795 👎 0

"""

import heapq
from queue import PriorityQueue
from typing import List

import pytest

from common_utils import ListNode


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        """
         O(N*logk) k是链表数目 ;LeetCode无法运行？
         O(n)
         """
        Q = PriorityQueue()
        for l in lists:
            if l:
                Q.put((l.val, l))
        dummyHead = ListNode(-1)
        cur_head = dummyHead
        while not Q.empty():
            val, node = Q.get()
            cur_head.next = ListNode(val)
            cur_head = cur_head.next
            node = node.next
            if node:
                Q.put((node.val, node))
        return dummyHead.next


class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        """Me  O(NlogN) """
        min_heap = []
        heapq.heapify(min_heap)
        for head in lists:
            while head:
                heapq.heappush(min_heap, head.val)
                head = head.next
        dummyHead = ListNode(-1)
        cur_head = dummyHead
        while min_heap:
            val = heapq.heappop(min_heap)
            cur_head.next = ListNode(val)
            cur_head = cur_head.next
        return dummyHead.next


@pytest.mark.parametrize("kw,expected", [
    [dict(lists=[
        ListNode.init_list_from_str("1->4->5"),
        ListNode.init_list_from_str("1->3->4"),
        ListNode.init_list_from_str("2->6")
    ]), ListNode.init_list_from_str("1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6")],
])
def test_solutions(kw, expected):
    assert repr(Solution().mergeKLists(**kw)) == repr(expected)
    assert repr(Solution1().mergeKLists(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
