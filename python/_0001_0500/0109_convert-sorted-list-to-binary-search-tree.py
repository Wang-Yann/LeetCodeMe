#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 22:24:09
# @Last Modified : 2020-04-27 22:24:09
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
#  示例:
#
#  给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  Related Topics 深度优先搜索 链表
#  👍 256 👎 0
import copy

import pytest

from common_utils import ListNode, TreeNode


class Solution:

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """ 前序方式"""
        cur, length = head, 0
        while cur:
            cur, length = cur.next, length + 1
        self.head = head
        return self.helper(0, length)

    def helper(self, start, end):
        if start == end:
            return None
        mid = (start + end) >> 1
        left = self.helper(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.helper(mid + 1, end)
        return current


class Solution1:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast, pre = head, head, None
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None  # cut off the left half

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([-10, -3, 0, 5, 9]), ['0', '-3', '9', '-10', '#', '5'])
])
def test_solutions(args, expected):
    assert repr(Solution().sortedListToBST(copy.deepcopy(args))) == repr(expected)
    assert repr(Solution1().sortedListToBST(copy.deepcopy(args))) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
