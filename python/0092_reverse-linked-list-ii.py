#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 20:29:48
# @Last Modified : 2020-04-18 20:29:48
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
#  说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#  Related Topics 链表
#  👍 425 👎 0

"""
import copy

import pytest

from common_utils import ListNode


class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i = 0
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while i < m - 1:
            cur = cur.next
            i += 1
        left_end = cur
        mid_stack = []
        while i < n:
            cur = cur.next
            mid_stack.append(ListNode(cur.val))
            i += 1
        right_part = cur.next
        for node in mid_stack[::-1]:
            left_end.next = node
            left_end = left_end.next
        left_end.next = right_part
        return dummy.next


class Solution1:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        diff, dummy, cur = n - m + 1, ListNode(-1), head
        dummy.next = head

        last_un_swap = dummy
        while cur and m > 1:
            cur, last_un_swap, m = cur.next, cur, m - 1
        prev, first_swap = last_un_swap, cur
        # print(first_swap, last_unswap, sep="\t")
        # print(cur, prev, sep="\t")
        # Reverse List part
        while cur and diff > 0:
            prev, cur.next, cur, diff = cur, prev, cur.next, diff - 1
        # print(cur.val, prev.val, sep="\t")
        # print(first_swap.val, last_unswap.val, sep="\t")

        first_swap.next, last_un_swap.next = cur, prev

        return dummy.next

    def reverseList(self, head):
        """
        TODO 示范写法
        """
        dummy = ListNode(-1)
        while head:
            # print("Before", head, dummy.next, head.next, sep="\t")
            dummy.next, head.next, head = head, dummy.next, head.next
            # print("After",dummy.next, head.next, head,sep="\t")
        return dummy.next

    def reverseListRec(self, head):
        """
         示范写法
        """
        if head.next is None:
            return head
        last = self.reverseListRec(head.next)
        head.next.next = last
        head.next = None
        return


class Solution2:

    def reverseBetween(self, head, m, n):

        if not head:
            return head

        left, right = head, head
        stop = False

        def recurseAndReverse(right_node, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right_node = right_node.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right_node, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right_node or right_node.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right_node.val = right_node.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head


class Solution3:
    """
    https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/bu-bu-chai-jie-ru-he-di-gui-di-fan-zhuan-lian-biao/
    """

    def __init__(self):
        # // 后驱节点
        self.successor = None

    def reverseBetween(self, head, m, n):
        if m == 1:
            # // 相当于反转前 n 个元素
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    # // 反转以 head 为起点的 n 个节点，返回新的头结点
    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        # // 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last


@pytest.mark.parametrize("kw,expected", [
    (dict(
        head=ListNode.initList([1, 2, 3, 4, 5]),
        m=2,
        n=4
    ), ListNode.initList([1, 4, 3, 2, 5]))
])
def test_solutions(kw, expected):
    kw1 = copy.deepcopy(kw)
    kw2 = copy.deepcopy(kw)
    kw3 = copy.deepcopy(kw)
    assert repr(Solution().reverseBetween(**kw)) == repr(expected)
    assert repr(Solution1().reverseBetween(**kw1)) == repr(expected)
    assert repr(Solution2().reverseBetween(**kw2)) == repr(expected)
    assert repr(Solution3().reverseBetween(**kw3)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
