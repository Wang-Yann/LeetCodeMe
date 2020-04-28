#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 22:24:09
# @Last Modified : 2020-04-27 22:24:09
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import ListNode, TreeNode


class Solution:
    head = None

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """ 前序方式"""
        cur, length = head, 0
        while cur:
            cur, length = cur.next, length + 1
        self.head = head
        return self.sortedListToBSTRecu(0, length)

    def sortedListToBSTRecu(self, start, end):
        if start == end:
            return None
        mid = (start + end) >> 1
        left = self.sortedListToBSTRecu(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sortedListToBSTRecu(mid + 1, end)
        return current


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ListNode.initList([-10, -3, 0, 5, 9])
    ]
    res = [sol.sortedListToBST(args) for args in samples]
    print(res)
