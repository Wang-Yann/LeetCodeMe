#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 19:42:09
# @Last Modified : 2020-05-10 19:42:09
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest

from common_utils import ListNode


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        ans, tailA, tailB = None, None, None
        while curA and curB:
            if curA is curB:
                ans = curA
                break
            if curA.next:
                curA = curA.next
            elif tailA is None:
                tailA = curA
                curA = headB
            else:
                break

            if curB.next:
                curB = curB.next
            elif tailB is None:
                tailB = curB
                curB = headA
            else:
                break
        return ans

class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1



def test_solutions():
    l1 = ListNode.initList([4, 1, 8, 4, 5])
    l2 = ListNode.initList([5, 0])
    l2.next.next = l1.next
    res =  Solution().getIntersectionNode(l1, l2)
    res1 =  Solution1().getIntersectionNode(l1, l2)
    assert res == l1.next
    assert res1 == l1.next


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
