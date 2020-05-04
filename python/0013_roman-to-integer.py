#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 13:14:03
# @Last Modified : 2020-05-04 13:14:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def romanToInt(self, s: str) -> int:
        numeral_map = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90,
                       'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        ans = 0
        i, length = 0, len(s)
        while i < length:
            if s[i:i + 2] in numeral_map:
                ans += numeral_map[s[i:i + 2]]
                i += 2
            elif s[i] in numeral_map:
                ans += numeral_map[s[i:i + 1]]
                i += 1
            else:
                break
        return ans


@pytest.mark.parametrize("expected,args", [
    (3, "III"),
    (4, "IV"),
    (9, "IX"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
])
def test_solutions(expected, args):
    assert Solution().romanToInt(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
