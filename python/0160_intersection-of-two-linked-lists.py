#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 15:20:08
# @Last Modified : 2020-04-19 15:20:08
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        方法二: 哈希表法
            遍历链表 A 并将每个结点的地址/引用存储在哈希表中。然后检查链表 B 中的每一个结点 b
            是否在哈希表中。若在，则 b​ 为相交结点。


        方法三：双指针法
            创建两个指针 pApA 和 pBpB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
            当 pApA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B); 类似的，当 pBpB 到达链表的尾部时，将它重定位到链表 A 的头结点。
            若在某一时刻 pApA 和 pBpB 相遇，则 pApA/pBpB 为相交结点。
            想弄清楚为什么这样可行, 可以考虑以下两个链表: A={1,3,5,7,9,11} 和 B={2,4,9,11}，相交于结点 9。 由于 B.length (=4) < A.length (=6)，
            pBpB 比 pApA 少经过 22   个结点，会先到达尾部。将 pBpB 重定向到 A 的头结点，pApA 重定向到 B 的头结点后，pBpB 要比 pApA 多走 2 个结点。
            因此，它们会同时到达交点。 如果两个链表存在相交，它们末尾的结点必然相同。
            因此当 pApA/pBpB 到达链表结尾时，记录下链表 A/B 对应的元素。若最后元素不相同，则两个链表不相交。


            链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/xiang-jiao-lian-biao-by-leetcode/
        """
        curA, curB = headA, headB
        begin, tailA, tailB = None, None, None

        while curA and curB:
            if curA is curB:
                begin = curA
                break
            if curA.next:
                curA = curA.next
            elif tailA is None:
                tailA = curA
                curA = headB
            else:
                break

            if curB.next:
                curB = curB.next
            elif tailB is None:
                tailB = curB
                curB = headA
            else:
                break
        return begin


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([4, 1], [5, 0, 1, 8, 4, 5])
    ]
    l1 = ListNode.initList([4, 1, 8, 4, 5])
    l2 = ListNode.initList([5, 0])
    cur_l2 = l2
    cur_l1 = l1.next
    cur_l2.next.next = cur_l1
    # res = [sol.getIntersectionNode(l1, l2) for x, y in samples]
    # print(res)
    res1 = [sol.getIntersectionNode(ListNode.initList(x), ListNode.initList(y)) for x, y in samples]
    print(res1)
