#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-10 18:40:02
# @Last Modified : 2020-05-10 18:40:02
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import functools

import pytest


class Solution:

    def translateNum(self, num: int) -> int:
        """
        递归出口是num是只有一位数，以xyzcba为例，先取最后两位（个位和十位）即ba，如果ba>=26，必然不能分解成f(xyzcb)+f(xyzc)，此时只能分解成f(xyzcb);但还有一种情况，就是ba<=9,也就是该数十位上为0，此时也不能分解

        """

        @functools.lru_cache(None)
        def dfs(n):
            if n <= 9:
                return 1
            ba = n % 100
            if ba <= 9 or ba >= 26:
                return dfs(n // 10)
            else:
                return dfs(n // 10) + dfs(n // 100)

        return dfs(num)


class Solution1:

    def translateNum(self, num: int) -> int:
        """
        GOOD
        https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
        """
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a


@pytest.mark.parametrize("args,expected", [
    (12258, 5),
])
def test_solutions(args, expected):
    assert Solution().translateNum(args) == expected
    assert Solution1().translateNum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])