#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 10:29:38
# @Last Modified : 2021-02-25 10:29:38
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。 
# 
#  请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。 
# 
#  下图中蓝色边和节点展示了操作后的结果： 
# 
#  请你返回结果链表的头指针。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# 输出：[0,1,2,1000000,1000001,1000002,5]
# 解释：我们删除 list1 中第三和第四个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。
#  
# 
#  示例 2： 
# 
#  
# 输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,100
# 0003,1000004]
# 输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]
# 解释：上图中蓝色的边和节点为答案链表。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= list1.length <= 104 
#  1 <= a <= b < list1.length - 1 
#  1 <= list2.length <= 104 
#  
#  Related Topics 链表 
#  👍 9 👎 0


import pytest

from common_utils import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = None, list1
        for i in range(b):
            if i == a - 1:
                start = end
            end = end.next
        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(list1=ListNode.initList([0, 1, 2, 3, 4, 5]),
          a=3, b=4, list2=ListNode.initList([1000000, 1000001, 1000002])),
     ListNode.initList([0, 1, 2, 1000000, 1000001, 1000002, 5])],
    [dict(list1=ListNode.initList([0, 1, 2, 3, 4, 5, 6]), a=2, b=5,
          list2=ListNode.initList([1000000, 1000001, 1000002, 1000003, 1000004]))
        , ListNode.initList([0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6])],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().mergeInBetween(**kw)
    assert repr(res) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
