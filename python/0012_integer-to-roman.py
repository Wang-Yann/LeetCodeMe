#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 13:14:03
# @Last Modified : 2020-05-04 13:14:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def intToRoman(self, num: int) -> str:
        numeral_map = {1:"I", 4:"IV", 5:"V", 9:"IX",
                       10:"X", 40:"XL", 50:"L", 90:"XC",
                       100:"C", 400:"CD", 500:"D", 900:"CM",
                       1000:"M"}
        keys, res = sorted(numeral_map.keys()), []
        while num > 0:
            for key in reversed(keys):
                while num >= key:
                    num -= key
                    res += [numeral_map[key]]
        return "".join(res)


@pytest.mark.parametrize("args,expected", [
    (3, "III"),
    (4, "IV"),
    (9, "IX"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
])
def test_solutions(args, expected):
    assert Solution().intToRoman(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
