#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 14:38:17
# @Last Modified : 2020-05-05 14:38:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n != 1:
            if n & 0b1 == 0: # 偶数直接右移
                n >>= 1
            else:
                #
                # 奇数+1或者-1，有两种选项。
                # 2.1 显然，让每一步1的数目最少好处大，于是 0bxxx01 采用 -1； 0bxxx11 采用 +1；
                # 2.2 特殊情况 3，按上述原则+1后两次右移共需3次；减一后只需一次右移共2次，因此3采用-1操作

                if n & 0b10 == 0 or n == 0b11:
                    n -= 1
                else:
                    n += 1
            cnt += 1
        return cnt


@pytest.mark.parametrize("args,expected", [
    (8, 3),
    (65535, 17),
    pytest.param(7, 4),
])
def test_solutions(args, expected):
    assert Solution().integerReplacement(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
