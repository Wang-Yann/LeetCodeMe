#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 22:58:07
# @Last Modified : 2020-04-19 22:58:07
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
#
#  如果有两个中间结点，则返回第二个中间结点。
#
#
#
#  示例 1：
#
#  输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next =
# NULL.
#
#
#  示例 2：
#
#  输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
#
#
#
#
#  提示：
#
#
#  给定链表的结点数介于 1 和 100 之间。
#
#  Related Topics 链表
#  👍 235 👎 0

"""
import pytest

from common_utils import ListNode


class Solution:

    def middleNode(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([1, 2, 3, 4, 5]), 3),
    (ListNode.initList([1, 2, 3, 4, 5, 6]), 4),
])
def test_solutions(args, expected):
    res = Solution().middleNode(args)
    assert res and res.val == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
