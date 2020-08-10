#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 17:08:00
# @Last Modified : 2020-04-22 17:08:00
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from collections import deque
from typing import List

import pytest

from common_utils import TreeNodeWithChildren as Node


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        results = []
        q = deque([root])
        level = 0
        while q:
            results.append([])
            length = len(q)
            for i in range(length):
                node = q.popleft()
                results[level].append(node.val)
                if node.children:
                    q.extend(node.children)
            level += 1
        return results


@pytest.mark.parametrize("kw,expected", [
    [dict(
        root=Node(1, [Node(3, [Node(5), Node(6)]),
                      Node(2),
                      Node(4)]
                  )
    ), [[1], [3, 2, 4], [5, 6]]],
])
def test_solutions(kw, expected):
    assert Solution().levelOrder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
