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
import pytest

from common_utils import ListNode, TreeNode


class Solution:
    head = None

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


@pytest.mark.parametrize("args,expected", [
    (ListNode.initList([-10, -3, 0, 5, 9]),
     ['0', '-3', '9', '-10', '#', '5'])
])
def test_solutions(args, expected):
    assert repr(Solution().sortedListToBST(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
