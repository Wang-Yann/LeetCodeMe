#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 22:02:39
# @Last Modified : 2020-05-04 22:02:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def addDigits(self, num: int) -> int:

        if num < 10:
            return num
        ans = 0
        while num:
            ans += num % 10
            num //= 10
        return self.addDigits(ans)


class Solution1:
    """
        不符合题目要求  O(1) 时间复杂度
        似乎可以通过n % 9得到最后的值
        但是有1个关键的问题，如果num是9的倍数，那么就不适用上述逻辑。原本我是想得到n被打包成10个1份的份数+打不进10个1份的散落个数的和。
        通过与9取模，去获得那个不能整除的1，作为计算份数的方式，但是如果可以被9整除，我就无法得到那个1，也得不到个位上的数。
        所以需要做一下特殊处理，(num - 1) % 9 + 1
        可以这么做的原因：原本可以被完美分成9个为一份的n样物品，我故意去掉一个，
        那么就又可以回到上述逻辑中去得到我要的n被打包成10个一份的份数+打不进10个一份的散落个数的和。
        而这个减去的1就相当于从，在10个1份打包的时候散落的个数中借走的，本来就不影响原来10个1份打包的份数，先拿走再放回来，都只影响散落的个数，
        所以没有关系。

    """

    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num > 0 else 0


@pytest.mark.parametrize("args,expected", [
    (38, 2),
    (0, 0),
    pytest.param(3, 3),
])
def test_solutions(args, expected):
    assert Solution().addDigits(args) == expected
    assert Solution1().addDigits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
