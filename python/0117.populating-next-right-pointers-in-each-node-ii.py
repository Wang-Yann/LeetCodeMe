#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-21 21:08:59
# @Last Modified : 2020-04-21 21:08:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNodeWithNext as Node


class Solution:



    def connect(self, root: 'Node') -> 'Node':
        """
        Good
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-28/
        """
        if not root:
            return root
        cur = root
        while cur:
            dummy = Node(-1)
            tail = dummy
            # //遍历 cur 的当前层
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = dummy.next
            # //更新 cur 到下一层
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        Node(1, Node(2, None, Node(5), None), Node(3, None, Node(7), None), None)
    ]
    res = [sol.connect(x) for x in samples]
    print(samples)
