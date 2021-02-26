#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 22:06:34
# @Last Modified : 2021-02-26 22:06:34
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你链表的头节点 head 和一个整数 k 。 
# 
#  交换 链表正数第 k 个节点和倒数第 k 个节点的值后，返回链表的头节点（链表 从 1 开始索引）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [7,9,6,6,7,8,3,0,9,5], k = 5
# 输出：[7,9,6,6,8,7,3,0,9,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1], k = 1
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：head = [1,2], k = 1
# 输出：[2,1]
#  
# 
#  示例 5： 
# 
#  
# 输入：head = [1,2,3], k = 2
# 输出：[1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目是 n 
#  1 <= k <= n <= 105 
#  0 <= Node.val <= 100 
#  
#  Related Topics 链表 
#  👍 7 👎 0
  

"""

import pytest, traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode, ListNode
from sample_datas import BIG_CASE


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """快慢指针 经典"""
        slow, fast = head, head

        for _ in range(k - 1):
            fast = fast.next
        first = fast
        while fast.next:
            slow, fast = slow.next, fast.next
        first.val, slow.val = slow.val, first.val
        return head


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 2, 3, 4, 5]), k=2), ListNode.initList([1, 4, 3, 2, 5])],
    [dict(head=ListNode.initList([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), k=5), ListNode.initList([7, 9, 6, 6, 8, 7, 3, 0, 9, 5])],
    [dict(head=ListNode.initList([1]), k=1), ListNode.initList([1])],
    [dict(head=ListNode.initList([1, 2]), k=1), ListNode.initList([2, 1])],
    [dict(head=ListNode.initList([1, 2, 3]), k=2), ListNode.initList([1, 2, 3])],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().swapNodes(**kw)
    assert repr(res) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])