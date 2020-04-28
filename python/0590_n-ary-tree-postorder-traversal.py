#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 17:08:00
# @Last Modified : 2020-04-22 17:08:00
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from typing import List

from common_utils import TreeNodeWithChildren as Node


class Solution0:
    def postorder(self, root: 'Node') -> List[int]:
        results = []

        def helper(node):
            if not node:
                return
            if node.children:
                for child in node.children:
                    helper(child)
            results.append(node.val)

        helper(root)

        return results


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        results = []
        stack = [(root, False)]
        while stack:
            cur, is_visited = stack.pop()
            if is_visited:
                results.append(cur.val)
            else:
                stack.append((cur, True))
                if cur.children:
                    for child in cur.children[::-1]:
                        stack.append((child, False))

        return results


if __name__ == '__main__':
    sol = Solution()
    samples = [
        Node(1, [Node(3, [Node(5), Node(6)]),
                 Node(2),
                 Node(4)]
             ),
        None,
        Node(1)

    ]
    res = [sol.postorder(x) for x in samples]
    print(res)
