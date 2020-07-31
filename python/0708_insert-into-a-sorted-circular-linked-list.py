#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 14:19:11
# @Last Modified : 2020-07-31 14:19:11
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素，使这个列表仍然是循环升序的。给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中
# 最小元素的指针。 
# 
#  如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。 
# 
#  如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个点。否则。请返回原先给定的节点。 
# 
#  下面的例子可以帮你更好的理解这个问题： 
# 
#  
# 
#  
#  
# 在上图中，有一个包含三个元素的循环有序列表，你获得值为 3 的节点的指针，我们需要向表中插入元素 2。 
# 
#  
# 
#  
#  
# 
#  新插入的节点应该在 1 和 3 之间，插入之后，整个列表如上图所示，最后返回节点 3。 
#  Related Topics 链表 
#  👍 15 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    情况 1： 新节点的值位于当前链表的最小值和最大值之间。因此，应该将其插入到链表中间。
    情况 2： 新值超出了链表中的最小值和最大值，即小于最小值或大于最大值。在任一情况下，新值都应插入在尾节点（即链表最大值的节点）之后
    情况 3： 链表的元素的值相同。 尽管在问题描述中没有说明，但是链表可能出现所有节点的值均相同
    还有一种情况，是当链表为空时，我们可以在进入循环之前解决它。



    """

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        prev, curr = head, head.next
        toInsert = False
        while True:
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            if toInsert:
                # mission accomplished
                prev.next = Node(insertVal, curr)
                return head
                # loop condition
            prev, curr = curr, curr.next
            if prev == head:
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head


# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    head = Node(3, Node(1, Node(4)))
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = head
    res = Solution().insert(head, 2)
    while res.next:
        print(res.val)
        res = res.next
        if res.val == 3:
            break


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
