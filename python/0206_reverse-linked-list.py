#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 16:27:07
# @Last Modified : 2020-04-19 16:27:07
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 反转一个单链表。
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#  进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#  Related Topics 链表
#  👍 1096 👎 0

"""
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
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        """TODO
        涉及到链表的操作，一定要在纸上把过程先画出来，再写程序
        https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode/
        假设列表的其余部分已经被反转，现在我该如何反转它前面的部分
        如 N1->N2->..->Nk->N(k+1)<-..<-Nm<- ∅
        我们正处于Nk
        所以
        Nk.next.next=Nk

        """
        if not (head and head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 2, 3, 4, 5])), ListNode.initList([1, 2, 3, 4, 5][::-1])],
    [dict(head=ListNode.initList([1, 2])), ListNode.initList([2, 1])],
    [dict(head=ListNode.initList([1])), ListNode.initList([1])],
])
@pytest.mark.parametrize("SolutionCLS", [Solution1, Solution2, Solution])
def test_solutions(kw, expected, SolutionCLS):
    assert repr(SolutionCLS().reverseList(**copy.deepcopy(kw))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
