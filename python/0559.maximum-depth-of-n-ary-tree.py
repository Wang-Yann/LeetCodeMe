#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 14:56:02
# @Last Modified : 2020-04-23 14:56:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


from common_utils import TreeNodeWithChildren as Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children:
            return 1
        return max([self.maxDepth(node) for node in root.children]) + 1


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
    lists = [x for x in samples]
    res = [sol.maxDepth(x) for x in lists]
    print(res)
