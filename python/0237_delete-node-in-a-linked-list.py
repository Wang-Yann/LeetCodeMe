#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-19 16:15:27
# @Last Modified : 2020-04-19 16:15:27
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([4, 5, 1, 9], 5),
        ([4, 5, 1, 9], 1)
    ]
    lists = [(ListNode.initList(x),y) for x, y in samples]
    res = [sol.deleteNode(x) for x, y in lists]
    print(lists)
