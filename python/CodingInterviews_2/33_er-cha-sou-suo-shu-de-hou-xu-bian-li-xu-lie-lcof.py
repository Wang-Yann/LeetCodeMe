#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-08 22:46:30
# @Last Modified : 2020-05-08 22:46:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(i, j):
            if i >= j:
                return True
            parent = i
            while postorder[parent] < postorder[j]:
                parent += 1
            mid = parent
            while postorder[parent] > postorder[j]:
                parent += 1
            return parent == j and helper(i, mid - 1) and helper(mid, j - 1)

        return helper(0, len(postorder) - 1)


@pytest.mark.parametrize("args,expected", [
    ([1, 6, 3, 2, 5], False),
    ([1, 3, 2, 6, 5], True),
])
def test_solutions(args, expected):
    assert Solution().verifyPostorder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
