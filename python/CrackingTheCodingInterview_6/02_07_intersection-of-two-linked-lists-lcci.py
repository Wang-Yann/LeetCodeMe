#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 14:46:33
# @Last Modified : 2020-07-12 14:46:33
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个
# 节点是同一节点（引用完全相同），则这两个链表相交。 示例 1： 输入：intersectVal = 8, listA = [4,1,8,4,5], listB 
# = [5,0,1,8,4,5], skipA = 2, skipB = 3 输出：Reference of the node with value = 8 输入
# 解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4
# ,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。 示例 2： 输入：intersectVal = 2, listA = [0
# ,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 输出：Reference of the node with v
# alue = 2 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为
#  [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。 示例 3： 输入：intersectVal = 0, listA
#  = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 输出：null 输入解释：从各自的表头开始算起，链表 A 为 [
# 2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。 解释：
# 这两个链表不相交，因此返回 null。 注意： 如果两个链表没有交点，返回 null 。 在返回结果后，两个链表仍须保持原有的结构。 可假定整个链表结构中没有循
# 环。 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。 Related Topics 链表 
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

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        return curB


# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    inter = ListNode.initList([1, 8, 4, 5])
    headA = ListNode.initList([4])
    headB = ListNode.initList([5, 0])
    headA.next = inter
    headB.next = inter
    res = Solution().getIntersectionNode(headA, headB)
    assert res == inter


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
