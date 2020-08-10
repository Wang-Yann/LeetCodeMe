#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 17:00:02
# @Last Modified : 2020-04-19 17:00:02
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
#
#  请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
#  示例 1:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
#
#
#  示例 2:
#
#  输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
#
#  说明:
#
#
#  应当保持奇数节点和偶数节点的相对顺序。
#  链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
#
#  Related Topics 链表
#  👍 210 👎 0
"""

import pytest

from common_utils import ListNode


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        TODO
        https://leetcode-cn.com/problems/odd-even-linked-list/solution/qi-ou-lian-biao-by-leetcode/
        我们用变量 head 和 odd_tail 保存奇链表的头和尾指针。 even_head 和 cur 保存偶链表的头和尾指针
        """
        if not (head and head.next):
            return head
        odd_tail, even, even_head = head, head.next, head.next
        while even and even.next:
            odd_tail.next = even.next
            odd_tail = odd_tail.next
            even.next = odd_tail.next
            even = even.next
        odd_tail.next = even_head
        return head


@pytest.mark.parametrize("args,expected", [
    (
        ListNode.initList([1, 2, 3, 4, 5]),
        ListNode.initList([1, 3, 5, 2, 4]),

    )
])
def test_solutions(args, expected):
    assert repr(Solution().oddEvenList(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
