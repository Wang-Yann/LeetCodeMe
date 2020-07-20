#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 23:29:58
# @Last Modified : 2020-05-05 23:29:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
#  示例1：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  限制：
#
#  0 <= 链表长度 <= 1000
#
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
#  Related Topics 分治算法
#  👍 36 👎 0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(-1)
        cur=dummy
        curl1,curl2 =l1,l2
        while curl1 and curl2:
            if curl1.val<=curl2.val:
                cur.next=curl1
                cur=cur.next
                curl1=curl1.next
            else:
                cur.next=curl2
                cur=cur.next
                curl2=curl2.next
        cur.next=curl1 if curl1 else curl2
        return dummy.next

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next


@pytest.mark.parametrize("l1,l2,expected", [
    (ListNode.init_list_from_str("1->2->4"),
     ListNode.init_list_from_str("1->1->2"),
     ListNode.init_list_from_str("1->1->1->2->2->4")
     ),
])
def test_solutions(l1,l2, expected):
    res= Solution1().mergeTwoLists(l1,l2)
    while res and expected:
        assert res.val==expected.val
        res,expected  =res.next,expected.next
    assert not res and not expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


