#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-17 17:21:23
# @Last Modified : 2020-04-17 17:21:23
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

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
            print("cur after recurse HEAD |",head,"\t\tCUR",cur)
            while cnt:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                cnt -= 1
            head = cur
        return head


if __name__ == '__main__':
    sol = Solution()
    sample = [
        # ("1->2->3->4->5", 2),
        ("1->2->3->4->5->6->7", 3)
    ]
    # for res in [sol.swapPairs(x) for x in s_list]:
    for res in [sol.reverseKGroupRec(ListNode.init_list_from_str(nd), k) for nd,k in sample]:
        print(res)
