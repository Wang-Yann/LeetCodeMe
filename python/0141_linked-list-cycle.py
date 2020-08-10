#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 13:30:44
# @Last Modified : 2020-04-19 13:30:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个链表，判断链表中是否有环。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#
#
#  示例 1：
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
#  示例 2：
#
#  输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
#  示例 3：
#
#  输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
#
#
#
#
#
#  进阶：
#
#  你能用 O(1)（即，常量）内存解决此问题吗？
#  Related Topics 链表 双指针
#  👍 678 👎 0

"""
import pytest

from common_utils import ListNode


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def test_solution():
    l = ListNode.initList([3, 2, 0, -4])
    assert not Solution().hasCycle(l)
    cur = l
    while cur.next:
        cur = cur.next
    cur.next = l
    assert Solution().hasCycle(l)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
