#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 17:28:46
# @Last Modified : 2020-04-19 17:28:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生
# 成多级数据结构，如下面的示例所示。
#
#  给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。
#
#
#
#  示例 1：
#
#  输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# 输出：[1,2,3,7,8,11,12,9,10,4,5,6]
# 解释：
#
# 输入的多级列表如下图所示：
#
#
#
# 扁平化后的链表如下图：
#
#
#
#
#  示例 2：
#
#  输入：head = [1,2,null,3]
# 输出：[1,3,2]
# 解释：
#
# 输入的多级列表如下图所示：
#
#   1---2---NULL
#   |
#   3---NULL
#
#
#  示例 3：
#
#  输入：head = []
# 输出：[]
#
#
#
#
#  如何表示测试用例中的多级链表？
#
#  以 示例 1 为例：
#
#   1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
#
#  序列化其中的每一级之后：
#
#  [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
#
#
#  为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。
#
#  [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
#
#
#  合并所有序列化结果，并去除末尾的 null 。
#
#  [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
#
#
#
#  提示：
#
#
#  节点数目不超过 1000
#  1 <= Node.val <= 10^5
#
#  Related Topics 深度优先搜索 链表
#  👍 109 👎 0

"""
import copy

import pytest

from common_utils import DoubleWithChildNode as Node


class SolutionMe:

    def flatten(self, head: 'Node') -> 'Node':
        """ 题意容易混淆"""
        if not head:
            return head
        node_list = []
        self.dfs(head, node_list)
        # print([x.val for x in node_list])
        length = len(node_list)
        for i in range(length):
            if i <= length - 2:
                node_list[i].next = node_list[i + 1]
            if i >= 1:
                node_list[i].prev = node_list[i - 1]
        return node_list[0]

    def dfs(self, head, node_list):
        if not head or head.val is None:
            return
        node_list.append(Node(head.val))
        if head.child:
            cld = head.child
            head.child = None
            self.dfs(cld, node_list)
        self.dfs(head.next, node_list)


class SolutionRec(object):

    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next

    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)


class Solution(object):
    """
       方法二：迭代的深度优先搜索

       """

    def flatten(self, head):
        if not head:
            return

        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next


@pytest.mark.parametrize("kw,expected", [
    [dict(
        head=Node.initList([[1, 2, 3, 4, 5, 6],
                            [None, None, 7, 8, 9, 10],
                            [None, None, None, 11, 12]])
    ), Node.initList([[1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]])],
])
def test_solutions(kw, expected):
    assert repr(Solution().flatten(**copy.deepcopy(kw))) == repr(expected)
    assert repr(SolutionMe().flatten(**copy.deepcopy(kw))) == repr(expected)
    assert repr(SolutionRec().flatten(**copy.deepcopy(kw))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
