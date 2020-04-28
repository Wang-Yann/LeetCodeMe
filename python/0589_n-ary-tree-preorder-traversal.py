#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 17:08:00
# @Last Modified : 2020-04-22 17:08:00
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from typing import List

from common_utils import TreeNodeWithChildren as Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        results = []
        stack = [root]
        while stack:
            cur = stack.pop()
            results.append(cur.val)
            children = cur.children
            if children:
                for child in children[::-1]:
                    stack.append(child)

        return results


if __name__ == '__main__':
    sol = Solution()
    samples = [
        Node(1, [Node(3, [Node(5), Node(6)]),
                 Node(2),
                 Node(4)
                 ]
             )

    ]
    res = [sol.preorder(x) for x in samples]
    print(res)
