#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。 
# 
#  进阶: 
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？ 
# 
#  示例: 
# 
#  
# // 初始化一个单链表 [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
# solution.getRandom();
#  
#  Related Topics 蓄水池抽样

"""
import random

import pytest

from common_utils import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    https://leetcode-cn.com/problems/linked-list-random-node/solution/xu-shui-chi-chou-yang-suan-fa-by-jackwener/

    """

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.__head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        当你遇到第 i 个元素时，应该有 1/i 的概率选择该元素，1 - 1/i 的概率保持原有的选择
        """
        reservoir = -1
        curr, n = self.__head, 0
        while curr:
            if random.randint(1, n + 1) == 1:
                reservoir = curr.val
            curr, n = curr.next, n + 1
        return reservoir


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    head = ListNode.initList(list(range(9)))
    sol = Solution(head)
    assert sol.getRandom()


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
