#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:51:45
# @Last Modified : 2020-05-04 20:51:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def countDigitOne(self, n: int) -> int:
        """https://leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode/



        将 i 从 1 遍历到 n，每次遍历 i 扩大 10 倍：
        (n/(i*10))*i 表示 i*10 位上1的个数

        min(max((n mod (i*10)) -i +1,0),i) 表示需要额外数的（i×10)位上 1 的个数

        """
        ans = 0
        pivot = 1
        while pivot <= n:
            divider = pivot * 10
            ans += (n // divider) * pivot + min(max(n % divider - pivot + 1, 0), pivot)
            pivot =divider
        return ans


@pytest.mark.parametrize("args,expected", [
    (13, 6),
    pytest.param(8, 1),
])
def test_solutions(args, expected):
    assert Solution().countDigitOne(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
