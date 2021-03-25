#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 00:35:29
# @Last Modified : 2020-04-20 00:35:29
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
#
#  请你返回该链表所表示数字的 十进制值 。
#
#
#
#  示例 1：
#
#
#
#  输入：head = [1,0,1]
# 输出：5
# 解释：二进制数 (101) 转化为十进制数 (5)
#
#
#  示例 2：
#
#  输入：head = [0]
# 输出：0
#
#
#  示例 3：
#
#  输入：head = [1]
# 输出：1
#
#
#  示例 4：
#
#  输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# 输出：18880
#
#
#  示例 5：
#
#  输入：head = [0,0]
# 输出：0
#
#
#
#
#  提示：
#
#
#  链表不为空。
#  链表的结点总数不超过 30。
#  每个结点的值不是 0 就是 1。
#
#  Related Topics 位运算 链表
#  👍 39 👎 0
import pytest

from common_utils import ListNode


class Solution:

    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)


class Solution1:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        ans = 0
        while cur:
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans


@pytest.mark.parametrize("args,expected", [
    [ListNode.initList([1, 0, 1], ), 5],
    [ListNode.initList([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], ), 18880],
    [ListNode.initList([0], ), 0],
    [ListNode.initList([1], ), 1],
    [ListNode.initList([0, 0], ), 0],
    [ListNode.initList([0, 0, 1, 1], ), 3],
    [ListNode.initList([]), 0],
])
def test_solutions(args, expected):
    assert Solution().getDecimalValue(args) == expected
    assert Solution1().getDecimalValue(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
