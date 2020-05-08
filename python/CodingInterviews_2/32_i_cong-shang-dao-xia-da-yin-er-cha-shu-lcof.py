#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-08 22:35:03
# @Last Modified : 2020-05-08 22:35:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:return []
        res =[]
        q=collections.deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node =q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

@pytest.mark.parametrize("args,expected", [
    (TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7))),
     [3,9,20,15,7]),
])
def test_solutions(args, expected):
    assert Solution().levelOrder(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


