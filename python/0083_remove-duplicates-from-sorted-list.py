#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-18 13:08:39
# @Last Modified : 2020-04-18 13:08:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
#  示例 1:
#
#  输入: 1->1->2
# 输出: 1->2
#
#
#  示例 2:
#
#  输入: 1->1->2->3->3
# 输出: 1->2->3
#  Related Topics 链表
#  👍 349 👎 0

"""
import pytest

from common_utils import ListNode


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        left = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur = cur.next
            else:
                left.next = cur
                left = cur
                cur = cur.next
        left.next = None
        return dummy.next


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 2, 3, 4, 5, 5])), ListNode.initList([1, 2, 3, 4, 5])],
    [dict(head=ListNode.initList([1, 1, 1, 2, 3])), ListNode.initList([1, 2, 3])],
])
def test_solutions(kw, expected):
    assert repr(Solution().deleteDuplicates(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
