#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 16:15:27
# @Last Modified : 2020-04-19 16:15:27
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#
#  现有一个链表 -- head = [4,5,1,9]，它可以表示为:
#
#
#
#
#
#  示例 1:
#
#  输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
#
#  示例 2:
#
#  输入: head = [4,5,1,9], node = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#
#
#
#
#  说明:
#
#
#  链表至少包含两个节点。
#  链表中所有节点的值都是唯一的。
#  给定的节点为非末尾节点并且一定是链表中的一个有效节点。
#  不要从你的函数中返回任何结果。
#
#  Related Topics 链表
#  👍 719 👎 0
import pytest

from common_utils import ListNode


class Solution:

    def deleteNode(self, node):
        """
        TODO SB 问题，没营养
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node_to_delete = node.next
            node.val = node_to_delete.val
            node.next = node_to_delete.next
            del node_to_delete


@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([4, 5, 1, 9]), ListNode.initList([5, 1, 9]))
])
def test_solutions(args, expected):
    Solution().deleteNode(args)
    assert repr(args) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
