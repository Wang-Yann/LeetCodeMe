#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 13:30:44
# @Last Modified : 2020-04-19 13:30:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#  说明：不允许修改给定的链表。
#
#
#
#  示例 1：
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
#  示例 2：
#
#  输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
#  示例 3：
#
#  输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#
#
#
#
#
#
#  进阶：
# 你是否可以不用额外空间解决此题？
#  Related Topics 链表 双指针
#  👍 542 👎 0

"""

from common_utils import ListNode


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1)
    ]
    res = [sol.detectCycle(ListNode.initList(x)) for x in samples]
    print(res)
