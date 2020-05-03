#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 15:20:17
# @Last Modified : 2020-05-03 15:20:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        i, j = 0, 1
        for v in A:
            if v % 2 == 1:
                res[j] = v
                j += 2
            else:
                res[i] = v
                i += 2
        return res


class Solution1:

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


@pytest.mark.parametrize("args,expected", [
    ([4, 2, 5, 7], [4, 5, 2, 7]),
])
def test_solutions(args, expected):
    res = Solution().sortArrayByParityII(args)
    for idx, v in enumerate(res):
        assert idx % 2 == v % 2
    res1 = Solution1().sortArrayByParityII(args)
    for idx, v in enumerate(res1):
        assert idx % 2 == v % 2


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
