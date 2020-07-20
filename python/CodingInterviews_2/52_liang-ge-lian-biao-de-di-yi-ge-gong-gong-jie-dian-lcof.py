#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 19:42:09
# @Last Modified : 2020-05-10 19:42:09
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 输入两个链表，找出它们的第一个公共节点。
#
#  如下面的两个链表：
#
#
#
#  在节点 c1 开始相交。
#
#
#
#  示例 1：
#
#
#
#  输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, s
# kipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1
# ,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
#
#
#
#  示例 2：
#
#
#
#  输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
#  1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4
# ]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#
#
#
#
#  示例 3：
#
#
#
#  输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而
#  skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#
#
#
#
#  注意：
#
#
#  如果两个链表没有交点，返回 null.
#  在返回结果后，两个链表仍须保持原有的结构。
#  可假定整个链表结构中没有循环。
#  程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
#  本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lis
# ts/
#
#  Related Topics 链表
#  👍 65 👎 0

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
