#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 22:01:23
# @Last Modified : 2020-04-27 22:01:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

class Solution:

    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i

        return abs(num) == 1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        -10,0,1,6,8,14,
        -2147483648
    ]
    res = [sol.isUgly(args) for args in samples]
    print(res)
