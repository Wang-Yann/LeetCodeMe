#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20
from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        v_sum = digits[i]+1
        carry = v_sum // 10
        digits[i] = v_sum % 10
        i -= 1
        while i >= 0:
            v_sum = digits[i] + carry
            digits[i] = v_sum % 10
            carry = v_sum // 10
            if not carry:
                break
            i-=1
        if carry:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))
    print(sol.plusOne([9, 9]))
    print(sol.plusOne([ 1]))
