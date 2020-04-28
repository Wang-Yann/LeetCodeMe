#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena, lenb = len(a), len(b)
        if lena < lenb:
            a = "0" * (lenb - lena) + a
        else:
            b = "0" * (lena - lenb) + b
        res = ""
        carry = 0
        i = max(lena, lenb) - 1
        while i >= 0:
            v_sum = int(a[i]) + int(b[i]) + carry
            carry = v_sum // 2
            res = str(v_sum % 2) + res
            i -= 1
        if carry:
            res = "1" + res
        return res


if __name__ == '__main__':
    sol = Solution()
    a = "1010"
    b = "1011"
    c = "11"
    d = "1"
    print(sol.addBinary(a, b))
    print(sol.addBinary(c, d))
