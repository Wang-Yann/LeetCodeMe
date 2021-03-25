#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 16:10:52
# @Last Modified : 2020-07-28 16:10:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 用一个 非空 单链表来表示一个非负整数，然后将这个整数加一。 
# 
#  你可以假设这个整数除了 0 本身，没有任何前导的 0。 
# 
#  这个整数的各个数位按照 高位在链表头部、低位在链表尾部 的顺序排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出: [1,2,4]
#  
#  Related Topics 链表 
#  👍 32 👎 0

"""
import copy

import pytest

from common_utils import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """TODO"""

        def helper(node):
            if not node:
                return 1
            carry = helper(node.next)
            sum_val = carry + node.val
            node.val = sum_val % 10
            return sum_val // 10

        if not head:
            return head
        carry = helper(head)
        if carry:
            res = ListNode(1)
            res.next = head
            return res
        return head


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def plusOne(self, head: ListNode) -> ListNode:
        # sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

            # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 2, 3])), ListNode.initList([1, 2, 4])],
    [dict(head=ListNode.initList([9, 9])), ListNode.initList([1, 0, 0])],
])
def test_solutions(kw, expected):
    head1 = copy.deepcopy(kw["head"])
    assert repr(Solution().plusOne(kw["head"])) == repr(expected)
    assert repr(Solution1().plusOne(head1)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
