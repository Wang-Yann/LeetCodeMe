#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 15:47:45
# @Last Modified : 2020-05-03 15:47:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def pancakeSort(self, A: List[int]) -> List[int]:
        """TODO 20200503 官方解答错误,题目有问题"""
        ans = []

        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1

        return ans



@pytest.mark.parametrize("args,expected", [
    ([3, 2, 4, 1], [3,4,2,3,1,2,1,1]),
    ([1, 2, 3], [3,3,2,2,1,1]),
])
def test_solutions(args, expected):
    assert Solution().pancakeSort(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
