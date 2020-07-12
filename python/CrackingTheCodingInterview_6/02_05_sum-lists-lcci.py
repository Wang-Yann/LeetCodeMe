#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 14:36:16
# @Last Modified : 2020-07-12 14:36:16
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定两个用链表表示的整数，每个节点包含一个数位。 
#  这些数位是反向存放的，也就是个位排在链表首部。 
#  编写函数对这两个整数求和，并用链表形式返回结果。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
# 输出：2 -> 1 -> 9，即912
#  
# 
#  进阶：假设这些数位是正向存放的，请再做一遍。 
# 
#  示例： 
# 
#  
# 输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
# 输出：9 -> 1 -> 2，即912
#  
#  Related Topics 链表 数学 
#  👍 24 👎 0


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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        ans = dummy
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            ans.next = ListNode(carry % 10)
            ans = ans.next
            carry //= 10
        if carry:
            ans.next = ListNode(carry)
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(l1=ListNode.initList([7, 1, 6]), l2=ListNode.initList([5, 9, 2])), ListNode.initList([2, 1, 9])],
    # [dict(l1=ListNode.initList([6, 1, 7]), l2=ListNode.initList([2, 9, 5])), ListNode.initList([9, 1, 2])],

])
def test_solutions(kwargs, expected):
    assert repr(Solution().addTwoNumbers(**kwargs)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
