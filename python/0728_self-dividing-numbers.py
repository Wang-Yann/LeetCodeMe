#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:00:44
# @Last Modified : 2020-05-05 18:00:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num):
            cur = num
            while cur:
                cur, rest = divmod(cur, 10)
                if rest ==0 or num % rest != 0:
                    return False
            return True

        ans = []
        for i in range(left, right + 1):
            if is_self_dividing(i):
                ans.append(i)
        return ans


@pytest.mark.parametrize("left,right,expected", [
    (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
])
def test_solutions(left, right, expected):
    assert Solution().selfDividingNumbers(left, right) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
