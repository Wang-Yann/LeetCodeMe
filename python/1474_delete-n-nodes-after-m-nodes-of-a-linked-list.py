#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 17:17:52
# @Last Modified : 2020-08-07 17:17:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定链表 head 和两个整数 m 和 n. 遍历该链表并按照如下方式删除节点: 
# 
#  
#  开始时以头节点作为当前节点. 
#  保留以当前节点开始的前 m 个节点. 
#  删除接下来的 n 个节点. 
#  重复步骤 2 和 3, 直到到达链表结尾. 
#  
# 
#  在删除了指定结点之后, 返回修改过后的链表的头节点. 
# 
#  进阶问题: 你能通过就地修改链表的方式解决这个问题吗? 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  输入: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
# 输出: [1,2,6,7,11,12]
# 解析: 保留前(m = 2)个结点,  也就是以黑色节点表示的从链表头结点开始的结点(1 ->2).
# 删除接下来的(n = 3)个结点(3 -> 4 -> 5), 在图中以红色结点表示.
# 继续相同的操作, 直到链表的末尾.
# 返回删除结点之后的链表的头结点. 
# 
#  示例 2: 
# 
#  
# 
#  输入: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
# 输出: [1,5,9]
# 解析: 返回删除结点之后的链表的头结点. 
# 
#  示例 3: 
# 
#  输入: head = [1,2,3,4,5,6,7,8,9,10,11], m = 3, n = 1
# 输出: [1,2,3,5,6,7,9,10,11]
#  
# 
#  示例 4: 
# 
#  输入: head = [9,3,7,7,9,10,8,2], m = 1, n = 2
# 输出: [9,7,8]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= 链表结点数 <= 10^4. 
#  [1 <= 链表的每一个结点值 <=10^6]. 
#  1 <= m,n <= 1000 
#  
#  Related Topics 链表 
#  👍 3 👎 0

"""
import copy

import pytest

from common_utils import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        pre = None
        while cur:
            p, q = m, n
            while p and cur:
                pre = cur
                cur = cur.next
                p -= 1
            while q and cur:
                cur = cur.next
                q -= 1
            pre.next = cur
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next:
            p, q = m, n
            while p and cur.next:
                cur = cur.next
                p -= 1
            while q and cur.next:
                cur.next = cur.next.next
                q -= 1
        return dummy.next


@pytest.mark.parametrize("kw,expected", [
    [dict(head=ListNode.initList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), m=2, n=3),
     ListNode.initList([1, 2, 6, 7, 11, 12])],
    [dict(head=ListNode.initList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), m=1, n=3), ListNode.initList([1, 5, 9])],
    [dict(head=ListNode.initList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), m=3, n=1),
     ListNode.initList([1, 2, 3, 5, 6, 7, 9, 10, 11])],
    [dict(head=ListNode.initList([9, 3, 7, 7, 9, 10, 8, 2]), m=1, n=2), ListNode.initList([9, 7, 8])],
])
def test_solutions(kw, expected):
    kw1 = copy.deepcopy(kw)
    res = Solution1().deleteNodes(**kw)
    res1 = Solution1().deleteNodes(**kw1)
    assert repr(res) == repr(expected)
    assert repr(res1) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
