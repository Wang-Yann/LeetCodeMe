#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 21:33:27
# @Last Modified : 2020-05-04 21:33:27
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        lookup = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four",
                  5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",
                  10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen",
                  15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen",
                  20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",
                  70:"Seventy", 80:"Eighty", 90:"Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]
        res, i = [], 0
        while num:
            cur = num % 1000
            if num % 1000:
                res.append(self.threeDigits(cur, lookup, unit[i]))
            num //= 1000
            i += 1
        print("Ret", num, res)
        return " ".join(res[::-1])

    def threeDigits(self, num, lookup, unit):
        res = []
        if num // 100:
            res = [lookup[num // 100] + " " + "Hundred"]
        if num % 100:
            res.append(self.twoDigits(num % 100, lookup))
        if unit != "":
            res.append(unit)
        return " ".join(res)

    def twoDigits(self, num, lookup):
        if num in lookup:
            return lookup[num]
        return lookup[(num // 10) * 10] + " " + lookup[num % 10]


@pytest.mark.parametrize("args,expected", [
    (123, "One Hundred Twenty Three"),
    (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
    (1234567891, "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"),
    pytest.param(12345, "Twelve Thousand Three Hundred Forty Five"),
])
def test_solutions(args, expected):
    assert Solution().numberToWords(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
