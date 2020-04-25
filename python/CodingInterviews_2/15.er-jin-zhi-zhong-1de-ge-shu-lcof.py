#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 23:51:06
# @Last Modified : 2020-04-25 23:51:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

class Solution0:

    def hammingWeight(self, n: int) -> int:
        e = 0b1
        ans = 0
        for i in range(32):
            if e & n != 0b0:
                ans += 1
            e <<= 1
        return ans


class Solution:

    def hammingWeight(self, n: int) -> int:
        """对于任意数字 n ，将 n 和 n - 1做与运算，会把最后一个 1的位变成 0"""
        ans = 0
        while n!=0b0:
            ans+=1
            n &= (n-0b1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        0b00000000000000000000000000001011,
        0b00000000000000000000000010000000,
        0b11111111111111111111111111111101

    ]
    res = [sol.hammingWeight(args) for args in samples]
    print(res)
