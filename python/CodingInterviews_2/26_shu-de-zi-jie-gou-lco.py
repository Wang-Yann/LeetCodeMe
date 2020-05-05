#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 23:53:21
# @Last Modified : 2020-05-05 23:53:21
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
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def helper(A,B):
            if not B: return True
            if not A or A.val!=B.val:return False
            return helper(A.left,B.left) and helper(A.right,B.right)
        return bool(A and B) and (
                helper(A,B)
                or self.isSubStructure(A.left,B)
                or self.isSubStructure(A.right,B)
        )


@pytest.mark.parametrize("args,expected", [
    [(TreeNode(1,TreeNode(2),TreeNode(3)), TreeNode(1,right=TreeNode(3))),True],
])
def test_solutions(args, expected):
    assert Solution().isSubStructure(*args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


