#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-17 17:21:23
# @Last Modified : 2020-04-17 17:21:23
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import pytest

from common_utils import ListNode


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
         Common
        """
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count :
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            #与剩下链表连接起来
            p.next = tmp
            # print("tmp",tmp,"|   head",head,"P",dummy)
            head = tmp

        return dummy.next


    def reverseKGroupRec(self, head: ListNode, k: int) -> ListNode:
        """
        TODO :
        尾插法。

        Recurse
        """
        cur = head
        # print("HEAD_RAW | ",cur)
        cnt = 0
        while cur and cnt != k:
            cur = cur.next
            cnt += 1
        # print("cur before recurse | ",head,cur,k)
        if cnt == k:
            cur = self.reverseKGroupRec(cur, k)
            # print("cur after recurse HEAD |",head,"\t\tCUR",cur)
            while cnt:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                cnt -= 1
            head = cur
        return head

class Solution1:
    """ 官方"""
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next



@pytest.mark.parametrize("args,expected", [
    ((ListNode.initList([1, 2, 3, 4, 5]), 2), ListNode.initList([2, 1, 4, 3, 5])),
    ((ListNode.initList([1, 2, 3, 4, 5]), 3), ListNode.initList([3,2,1,4,5])),
])
def test_solutions(args, expected):
    assert repr(Solution().reverseKGroup(*args)) == repr(expected)



@pytest.mark.parametrize("args,expected", [
    ((ListNode.initList([1, 2, 3, 4, 5]), 2), ListNode.initList([2, 1, 4, 3, 5])),
    ((ListNode.initList([1, 2, 3, 4, 5]), 3), ListNode.initList([3,2,1,4,5])),
])
def test_solutions1(args, expected):
    assert repr(Solution().reverseKGroupRec(*args)) == repr(expected)


@pytest.mark.parametrize("args,expected", [
    ((ListNode.initList([1, 2, 3, 4, 5]), 2), ListNode.initList([2, 1, 4, 3, 5])),
    ((ListNode.initList([1, 2, 3, 4, 5]), 3), ListNode.initList([3,2,1,4,5])),
])
def test_solutions1(args, expected):
    assert repr(Solution1().reverseKGroup(*args)) == repr(expected)



if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
