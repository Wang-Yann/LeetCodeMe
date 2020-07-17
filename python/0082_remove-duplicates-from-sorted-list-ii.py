#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 13:08:39
# @Last Modified : 2020-04-18 13:08:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
#  示例 1:
#
#  输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
#  示例 2:
#
#  输入: 1->1->1->2->3
# 输出: 2->3
#  Related Topics 链表
#  👍 319 👎 0

"""

from common_utils import ListNode


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        left = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
            else:
                left.next = cur
                left = cur
                cur = cur.next
        left.next = None
        return dummy.next

    def deleteDuplicatesO(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val == cur.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "1->2->3->3->4->4->5",
        "1->1->1->2->3"
    ]
    res = [sol.deleteDuplicates(ListNode.init_list_from_str(x)) for x in samples]
    print(res)
