#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 22:07:15
# @Last Modified : 2020-05-02 22:07:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#
#  返回删除后的链表的头节点。
#
#  注意：此题对比原题有改动
#
#  示例 1:
#
#  输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
#
#  示例 2:
#
#  输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#
#
#
#
#  说明：
#
#
#  题目保证链表中节点的值互不相同
#  若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
#
#  Related Topics 链表
#  👍 30 👎 0

import pytest

from common_utils import ListNode


class Solution:

    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                break
            prev, cur = cur, cur.next
        prev.next = cur.next
        return dummy.next


@pytest.mark.parametrize("head,val,expected", [
    (ListNode.initList([4, 5, 1, 9]), 5, ListNode.initList([4, 1, 9]))
])
def test_solutions(head, val, expected):
    res = Solution().deleteNode(head, val)
    while res and expected:
        assert res.val == expected.val
        res, expected = res.next, expected.next
    assert res is None and expected is None


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
