#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 14:53:38
# @Last Modified : 2020-07-12 14:53:38
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一个有环链表，实现一个算法返回环路的开头节点。 有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。 示例 1
# ： 输入：head = [3,2,0,-4], pos = 1 输出：tail connects to node index 1 解释：链表中有一个环，其尾部连
# 接到第二个节点。 示例 2： 输入：head = [1,2], pos = 0 输出：tail connects to node index 0 解释：链表中有
# 一个环，其尾部连接到第一个节点。 示例 3： 输入：head = [1], pos = -1 输出：no cycle 解释：链表中没有环。 进阶： 你是否可以不
# 用额外空间解决此题？ Related Topics 链表 
#  👍 19 👎 0


"""

import pytest

from common_utils import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow


# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    head = ListNode.initList([3, 2, 0, -4])
    cur = head
    while cur.val != 0:
        cur = cur.next
    cur.next = head
    res = Solution().detectCycle(head)
    assert res.val == 3


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
